# public functions (accessible without credentials)
from api import getWidgetDataLatestCollections, getWidgetUrlsLatestCollections, getWidgetDataLatestContributors, getWidgetUrlsLatestContributors, getUserPublic

# account functions (requires username and password to be set in config.py)
from api import initializeSession, endSession, getUser

# helper functions
from api import getCollectionUrls, getUrlCountTotal, getUrlCountMap, getUrlCollectionNames, getUrlCollectionByName, getUrlsWithString

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

# print the urls of the latest publicly updated URL collections
print("\nattempting to get the urls of the latest updated URL collections . . .\n")
print(getWidgetUrlsLatestCollections())

# print the urls of the latest public contributors
print("\nattempting to get the urls of the latest contributors . . .\n")
print(getWidgetUrlsLatestContributors())

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

# print the names of a user's URL collections
names = getUrlCollectionNames(user["user"])
print(names)

# print the user's URL collection with a matching name
item = getUrlCollectionByName(user["user"], "⚙️ Systems Design")
print(item)

# print the URLs in a collection object
urls = getCollectionUrls(item)
print(urls)

# print the URLs in a collection object containing a query string
queriedUrls = getUrlsWithString(item, "microservice")
print(queriedUrls)

# print the total number of URLs in a user account
total = getUrlCountTotal(user["user"])
print(total)

# print the mapping of URL count per collection in a user account
map = getUrlCountMap(user["user"])
print(map)

# exit the session
endSession()

input()