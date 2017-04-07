import urllib
from BeautifulSoup import *

url = raw_input('Enter url - ')
position = raw_input('Enter position - ')
process = raw_input('Enter the number of times you want do repeat the process - ')

num = int(position)
process = int(process)

print 'Retreiving: -', url 
times = 0
while times < process:
	html = urllib.urlopen(url).read()
	soup = BeautifulSoup(html)
	tags = soup('a')
	times = times + 1
	count= 0
	for tag in tags:
	    url2 = tag.get('href', None)
	    count = count + 1
	    if count is num:
	    	print  'Retreiving: -', url2
	    	url=url2
	    continue
	continue
