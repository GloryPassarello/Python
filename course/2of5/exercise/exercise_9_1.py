e_mail = open('mbox-short.txt')
days = dict()
t= list()
for line in e_mail:
	if line.startswith('From '):
		words = line.split()
		for x in words:
			if x == words[2] : 
				t.append(x)
print t
for c in t:
	days[c] = days.get(c, 0) + 1
print days
		
#print days