# imports
from api import getUserPublic
import json

# configs
outputDir = './output'
users = ['senaonp', 'senaonpNian']

# application logic
def filterData(data):
	del data['valid']
	for item in data['collections']:
		for attr in ['idx', 'public', 'updated']:
			del item[attr]
	return data

for user in users:
	print(f'generating file for {user}...')
	data = filterData(getUserPublic(user))
	newData = json.dumps(data, indent=4, ensure_ascii=False)
	datafile = open(f"{outputDir}/{user}.json", 'w+', encoding='utf-8')
	datafile.write(newData)
	datafile.close()
	print(f'finished generating file for {user}')
