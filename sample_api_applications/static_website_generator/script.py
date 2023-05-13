# imports
from api import getUserPublic
import json

# configs
outputDir = './output'
users = ['senaonp', 'senaonpNian']

# html element generator functions
def divType1(k,v):
	return f"""
		<p style='padding: 2px'>
			{str(k)} — <span style='font-size:1.1em'>{str(v)}</span>
		</p>
	"""
	
def divType2(item):
	header = f"""
		<hr />
		<p style='font-size: 1.1em; margin-bottom:5px; background-color: rgb(200,200,200); padding: 5px'>
			{item['name']} — {item['description']}
		</p>
	"""
	content = "<table style='border-collapse: collapse; margin-bottom: 20px'>"
	urls = []
	for url in item['urls']:
		urls.append(
			f"""
				<tr>
					<td style='border: 2px solid rgb(50,50,50)'; padding: 5px><a href='{url['url']}'>{url['url']}</a></td>
					<td style='border: 2px solid rgb(50,50,50); padding: 5px'>{url['urlName']}</td>
					<td style='border: 2px solid rgb(50,50,50); padding: 5px'>{url['urlDescription']}</td>
				</tr>
			""")
	content += ''.join(urls)+"</table>"
	return header + content

# application logic
skipAttrs = ['valid']

for user in users:
	print(f'generating file for {user}...')
	data = getUserPublic(user)
	datafile = open(f"{outputDir}/{user}.html", 'w+', encoding='utf-8')
	datafile.write('<html><body style="font-family:arial">')
	for k, v in data.items():
		if k in skipAttrs:
			continue
		if isinstance(v, list):
			for item in v:
				datafile.write(divType2(item))
			continue
		datafile.write(divType1(k,v))
	datafile.write('</body></html>')
	datafile.close()
	print(f'finished generating file for {user}')
