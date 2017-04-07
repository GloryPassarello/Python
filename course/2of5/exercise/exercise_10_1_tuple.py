u_input = raw_input('Please, enter a file: ')
if len(u_input) < 1 : u_input = 'mbox-short.txt'
text = open(u_input)
person = list()
ist = dict()
for line in text: 
	if line.startswith('From: '):
		d = line.split()
		p = d[1]
		person.append(p)
for x in person:
	ist[x] = ist.get(x, 0) + 1 
print 'the istogram count of the commints of the people from the the file insert: ', ist

tmp=list()
for k, v in ist.items():
	tmp.append((v, k)) #double parenthesis because we want a list of tuples
tmp.sort(reverse=True)
print 'list sorted: ', tmp

most_commit = tmp[0]
count, name = most_commit
print 'the person with more commits is: ', name, 'with a count of sent e-mail: ', count
