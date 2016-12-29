#Write a Python program to check that a string contains only a certain set of characters (in this case a-z, A-Z and 0-9)

text = open("text.txt")
txt=text.read()
import re
m = re.findall('[a-zA-Z0-9]',txt) #it returns a list
print m, type(m)