#copy the grep function
text=open("mbox.txt")
word = raw_input('Enter a regular expression: ')
import re
m=list()
for line in text:
	line = line.rstrip()
	if re.search(word, line): m.append(word)
count = len(m)
print "there are", count, "line that matches", word
