text = open('/home/anabrs1/Python_material/code/mbox.txt')
person = list()
ist = dict()
for line in text: 
	if line.startswith('From: '):
		d = line.split()
		p = d[1]
		person.append(p)
for x in person:
	ist[x] = ist.get(x, 0) + 1 
print ist 

bigword = None
bigcount = None
for word,count in ist.items(): #we can parse a list not a dictionary
	if bigcount is None or count > bigcount:
		bigword = word
		bigcount = count
print bigword, bigcount
