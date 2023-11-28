# public functions (accessible without credentials)
from api import getUserPublic

# helper functions
from api import getUrlCountTotal, getUrlCountMap

# other imports
import json
from urllib.parse import urlparse

# configs
outputDir = './output'
users = ['senaonp', 'senaonpNian']

# helper functions
def sortObj(d):
	r = []
	for k, v in d.items():
		r.append([k, v])
	b = False
	while b == False:
		b = True
		for i in range(len(r)-1):
			if r[i+1][1] > r[i][1]:
				m = r.pop(i+1)
				r.insert(i, m)
				b = False
	return r

# get url data by attribute
def getAllUrlsAttr(d, attr):
	r = {}
	for collection in d['collections']:
		for url in collection['urls']:
			u = getattr(urlparse(url['url']), attr)
			if u not in r.keys():
				r[u] = 1
			else:
				r[u] += 1
	return sortObj(r)

# application logic
def getStats(user):
	stats = []
	data = getUserPublic(user)
	dataPoints = [
		getUrlCountTotal(data), 
		getUrlCountMap(data)
	]
	stats.append(['profileName', data['name']])
	stats.append(['profileSize', f'{len(json.dumps(data))} chars'])
	stats.append(['totalUrlCount', dataPoints[0]])
	stats.append(['urlCollectionCount', len(dataPoints[1].keys())])
	stats.append(['urlCountPerCollection', sortObj(dataPoints[1])])
	stats.append(['urlDomainCount', getAllUrlsAttr(data, 'netloc')])
	stats.append(['urlSchemeCount', getAllUrlsAttr(data, 'scheme')])
	return stats

for user in users:
	stats = getStats(user)
	print(f'generating file for {user}...')
	datafile = open(f"{outputDir}/{user}.txt", 'w+', encoding='utf-8')
	for stat in stats:
		if isinstance(stat[1], list):
			datafile.write(f"{stat[0]}:\n")
			for s in stat[1]:
				datafile.write(f"\t({s[0]}): {s[1]}\n")
		else:
			datafile.write(f"{stat[0]}: {stat[1]}\n")
	datafile.close()
	print(f'finished generating file for {user}')
