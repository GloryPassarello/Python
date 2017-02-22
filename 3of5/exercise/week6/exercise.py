import urllib
import json

url = raw_input('Enter your URL - ')

print 'Retrieving', url
url2 = urllib.urlopen(url)

data= url2.read() #reads tha data and gives a string like output

js = json.loads(data) #reads the string and gives back a dictionary

#print json.dumps(js, indent=4)
 
#print 'Retrieved ', len(js['comments']) , 'characters'

counts=int()
for ogg in js['comments']:
	count = ogg['count']
	counts = counts + count
print 'Summary: ', counts
