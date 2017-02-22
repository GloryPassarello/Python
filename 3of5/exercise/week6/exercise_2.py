import urllib
import json

serviceurl = 'http://python-data.dr-chuck.net/geojson?'

while True:
	location = raw_input('Enter location: ')
	if len(location) <1 : break
	url = serviceurl + urllib.urlencode({'sensor':'false', 'address' : location })
	print 'Retriving', url 
	url2= urllib.urlopen(url)

	data = url2.read()

	try: js = json.loads(data)

	except: js = None
	if 'status' not in js or js['status'] != 'OK':
		print '==== Failure to Retrieve ===='
		print data
		continue

	#print json.dumps(js, indent=4)
	place_id = js['results'][0]['place_id']
	print 'place_id: ',place_id