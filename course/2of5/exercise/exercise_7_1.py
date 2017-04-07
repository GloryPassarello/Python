file_name = raw_input("Enter a file with the absolte path: ")
#file_text = open('/home/anabrs1/Python_material/code/mbox-short.txt')
try:
	file_text = open(file_name)
except:
	print "You should insert the name with the path."
	exit()
inp = file_text.read()
INP = inp.upper()
print INP