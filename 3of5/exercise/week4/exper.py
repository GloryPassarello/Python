import urllib
from BeautifulSoup import *

url = raw_input('Enter url - ')
position = raw_input('Enter position - ')
process = raw_input('Enter the number of times you want do repeat the process - ')

num = int(position)
process = int(process)
#print type(position)
html = urllib.urlopen(url).read()

print html


print 'Retreiving: -', url 
times = 0
while times < process:
	print 'we are fetching', url
	html = urllib.urlopen(url).read()
	soup = BeautifulSoup(html)
	tags = soup('a')
	times = times + 1
	count= 0
	for tag in tags:
	    url = tag.get('href', None)
	    count = count + 1
	    if count is num:
	    	print  'Retreiving: -', url
	    	print count
	    	#url=url2
	    continue
	continue
