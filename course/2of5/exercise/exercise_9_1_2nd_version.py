e_mail = open('mbox-short.txt')
days = dict()
t= list()
for line in e_mail:
	if line.startswith('From '):
		words = line.split()
		d = words[2]
		t.append(d)
print 'created a list with all the days of the week'
print t	
for c in t:
	days[c]=days.get(c, 0) + 1
print 'Each days appears on the list: ', days 
