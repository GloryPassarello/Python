#Write a Python program that matches a string that has an a followed by zero or more b's. - See more at: http://www.w3resource.com/python-exercises/re/#EDITOR
text = open('text.txt')
txt=text.read()
import re
m=re.findall('ab*', txt)
#ab*? would be not greedy so it would be print only a
#print m
#Write a Python program that matches a word containing 'b'
d=re.findall('\S+b\S+',txt)
print d