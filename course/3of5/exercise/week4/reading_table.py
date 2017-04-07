import urllib
from BeautifulSoup import *

url = raw_input('Enter - ')
html = urllib.urlopen(url).read()

print html

soup = BeautifulSoup(html)
# Retrieve all of the anchor tags
tags = soup('span')
count = 0
summary = int()
for tag in tags:
    # Look at the parts of a tag
    #print 'TAG:',tag
    #print 'URL:',tag.get('href', None)
    #print 'Contents:',tag.contents[0]
    #print 'Attrs:',tag.attrs
    num = int(tag.contents[0])
    count = count + 1 
    summary = summary + num
print 'Count: ', count
print 'Sum: ', summary