from api_config import username, password, domain
import requests
import os

# -------------------------------------------------
# ------------ public API data getters ------------
# -------------------------------------------------

def search(queryString):
	#r = requests.get(domain+"search/")
	#data = { "name": queryString }
	#r = requests.post(endpoint, json=data)
	#return r.json()
	return

def getWidgetData(endpoint):
	r = requests.get(domain+endpoint)
	return r.json()

# get public widget data for latest updated URL collections
def getWidgetDataLatestCollections():
	return getWidgetData("getWidgetDataLatestCollections")

# get public widget data for latest contributors
def getWidgetDataLatestContributors():
	return getWidgetData("getWidgetDataLatestContributors")

# get public widget urls for latest updated URL collections
def getWidgetUrlsLatestCollections():
	return ["https://haihai.link/viewCollection/"+item["user"]+"/"+item["name"].replace(" ", "_") for item in getWidgetDataLatestCollections()["data"]]

# get public widget urls for latest contributors	
def getWidgetUrlsLatestContributors():
	return ["https://haihai.link/viewUser/"+item["user"] for item in getWidgetDataLatestContributors()["data"]]

# get url collection for the webapp resources
def getWebsiteResources():
	return getUrlCollectionByName(getUserPublic("haihai"), "haihai.link")["urls"]

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

# ------------------------------------------------------
# ------------------ helper functions ------------------
# ------------------------------------------------------

# input: user [a user object], name [name of a URL collection]
# returns: a URL collection object
def getUrlCollectionByName(user, name):
	for item in user["collections"]:
		if item["name"] == name:
			return item
	print("cannot find URL collection with name ["+name+"]")
	return {}

# input: obj [a URL collection object]
# returns: a list of URLs
def getCollectionUrls(obj):
	if not obj or not obj["urls"]:
		print("cannot find urls in URL collection")
		return []
	return [item["url"] for item in obj["urls"]]
	
# input: user [a user object]
# returns: a list of URL collection names belonging to a user
def getUrlCollectionNames(user):
	return [item["name"] for item in user["collections"]]

# input: user [a user object]
# returns: the total number of URLs for a user
def getUrlCountTotal(user):
	c = 0
	for collection in user["collections"]:
		c += len(collection["urls"])
	return c

# input: user [a user object]
# returns: a mapping of URL collection name and corresponding number of URLs
def getUrlCountMap(user):
	m = {}
	for collection in user["collections"]:
		m[collection["name"]] = len(collection["urls"])
	return m

# input: user [a user object]
# returns: a mapping of URL collection name and it's associated data
def getUrlCollectionMap(user):
	m = {}
	for collection in user["collections"]:
		m[collection["name"]] = collection
	return m

# input: obj [a URL collection object], s [query string]
# returns: a list of url objects containing a matching string in it's attribute values
def getUrlsWithString(obj, s):
	r = []
	if not obj or not obj["urls"]:
		print("cannot find urls in URL collection")
		return r
	for url in obj["urls"]:
		if s.lower() in "".join(url.values()).lower():
			r.append(url)
	return r
