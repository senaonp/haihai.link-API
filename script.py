# public functions (accessible without credentials)
from haihai import getWidgetDataLatestCollections, getWidgetDataLatestContributors, getUserPublic

# account functions (requires username and password to be set in config.py)
from haihai import initializeSession, endSession, getUser

# helper functions
from haihai import getUrlCountTotal, getCollectionUrls, getUrlCountMap, getUrlCollectionByName

# --------------------------------------------------
# -------- haihai.link public api examples ---------
# --------------------------------------------------

# print the public information of user "isomer"
print("\nattempting to get public info of user 'isomer' . . .\n")
userPublicData = getUserPublic("isomer")
print(userPublicData)

# print the public information of user "haihai"
print("\nattempting to get public info of user 'haihai' . . .\n")
userPublicData = getUserPublic("haihai")
print(userPublicData)

# print the latest publicly updated URL collections
print("\nattempting to get latest updated URL collections . . .\n")
print(getWidgetDataLatestCollections())

# print the latest public contributors
print("\nattempting to get latest contributors . . .\n")
print(getWidgetDataLatestContributors())

# --------------------------------------------------
# ------------ haihai.link api examples ------------
# --------------------------------------------------

# initialize a session
sessionToken = initializeSession()
if not sessionToken:
	exit()

# get all of the user's details
user = getUser(sessionToken)
print(user)

# print the user's collections
userUrlCollections = user["user"]["collections"]
print(userUrlCollections)

# print the user's URL collection with a matching name
item = getUrlCollectionByName(user["user"], "💻 Computer Science")
print(item)

# print the URLs in a collection object
urls = getCollectionUrls(item)
print(urls)

# print the total number of URLs in a user account
total = getUrlCountTotal(user["user"])
print(total)

# print the mapping of URL count per collection in a user account
map = getUrlCountMap(user["user"])
print(map)

# exit the session
endSession()

input()