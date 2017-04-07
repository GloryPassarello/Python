#write a while loop that starts at the last character in the string and works its way backwards to the first character in the string 
#print the letter on a separate line, except backwards

name = 'Gloria Passarello'
index = len(name) -1
while index >= 0:
	letter = name[index]
	print letter
	index = index - 1

