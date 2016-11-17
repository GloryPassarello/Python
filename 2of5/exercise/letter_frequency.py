file = raw_input('Please, inser a file text:')
if len(file) < 1 : file = 'mbox-short.txt'
txt = open (file)
lett =list()
tmp=list()
for line in txt:
	tmp = line.split()
	if tmp == [] : continue  #removing blank line
	else: print tmp

 
