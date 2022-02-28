from api_config import username, password, domain
import requests
import os

# -------------------------------------------------
# ------------ public API data getters ------------
# -------------------------------------------------

def getWidgetData(endpoint):
	r = requests.get(domain+endpoint)
	return r.json()

# public widget data for latest updated URL collections
def getWidgetDataLatestCollections():
	return getWidgetData("getWidgetDataLatestCollections")

# public widget data for latest contributors
def getWidgetDataLatestContributors():
	return getWidgetData("getWidgetDataLatestContributors")

# get public information of any haihai.link username
def getUserPublic(username):
	endpoint = domain+"getUserPublic"
	data = { "name": username }
	r = requests.post(endpoint, json=data)
	return r.json()

# ------------------------------------------------------
# --------------- haihai.link session API --------------
# ------------------------------------------------------

def handleError():
	print("error: there appears to be an error getting data; please verify the username and password is valid for an account for haihai.link in the file 'api_config.py'; the current configured username is: ["+username+"]; the current configured password is: ["+password+"]")
	os.system('pause')
	exit()

def initializeSession():
	print("\nlogging in and setting session token . . .")
	endpoint = domain+"updateUserToken"
	data = {
		"name": username,
		"password": password,
		"action": "add"
	}
	r = requests.post(endpoint, json=data)
	if not r:
		handleError()
	else:
		response = r.json()
		if response and response["valid"]:
			token = response["token"]
			print("successfully set session token")
			return token
		else:
			handleError()

def endSession():
	print("\nlogging out and clearing session token . . .")
	endpoint = domain+"updateUserToken"
	data = {
		"name": username,
		"password": password,
		"action": "remove"
	}
	r = requests.post(endpoint, json=data)
	if not r:
		handleError()
	else:
		response = r.json()
		if response and response["valid"]:
			print("successfully cleared session token")
		else:
			handleError()

def getUser(token):
	endpoint = domain+"getUser"
	data = {
		"name": username,
		"token": token
	}
	r = requests.post(endpoint, json=data)
	if not r:
		handleError()
	return r.json()

def getUrlCollectionByName(user, name):
	obj = user["user"]["collections"]
	for item in obj:
		if item["name"] == name:
			return item
	print("cannot find URL collection with name ["+name+"]")
	return
