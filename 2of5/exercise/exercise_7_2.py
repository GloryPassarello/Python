file_name = raw_input("Enter a file with the absolte path: ")
#file_text = open('/home/anabrs1/Python_material/code/mbox-short.txt')
try:
	file_text = open(file_name)
except:
	print "You should insert the name with the path."
	exit()

#inp = file_text.read()
count = 0
tot = 0
for line in file_text:
	if line.startswith('X-DSPAM-Confidence:'):
		colon = line.find(':')
		num = float(line[colon+1:])
		count = count +1
		tot = tot + num 
		print 'spam number: ', num, 'count of line with spam: ', count, 'total of spam: ', tot
		
#average = sum(num)/count
print 'Average spam confidence: ', tot / count 

