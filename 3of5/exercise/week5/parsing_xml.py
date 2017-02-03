import urllib
import xml.etree.ElementTree as ET

url = raw_input('Enter your URL - ')
data = urllib.urlopen(url).read()
tree= ET.fromstring(data)

lst = tree.findall('comments/comment')

summ = int()
counting = int()
print 'Retriving ', url
for item in lst:
    cnt = int(item.find('count').text)
    summ = summ +  cnt
    counting = counting + 1
print 'Count', counting
print 'Sum: ', summ
