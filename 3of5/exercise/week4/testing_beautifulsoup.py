import urllib
from BeautifulSoup import *

url = 'https://www.crummy.com/software/BeautifulSoup/bs4/doc'
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)


#print soup.prettify()  

print soup.title # to see the title of the page
print soup.title.name
print soup.title.string
print soup.a
#print soup.find_all('a')

print(soup.get_text())