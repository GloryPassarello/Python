name = raw_input('Please, enter a file: ')
if len(name) < 1 : name = '/home/anabrs1/Python_material/code/mbox.txt'
txt = open(name)

t1=list()
for line in txt:
	if line.startswith('From '):
		d = line.split()
		hour = d[5].split(':')
        t1.append(hour[0])
		#print line.rstrip('\n')


ist=dict() #we create a dictionary that in reality is a instogramm
for h in t1:
	ist[h]= ist.get(h, 0) + 1

#z=ist.items() #it returns a list of tuples
tmp=list()
for k, v in ist.items():
	tmp.append((v, k))
tmp.sort(reverse=True)
print tmp

c, hr = tmp[0] #it is important to add a single tuple on this line otherwise this commands won't work 
for c, hr in tmp:
	print 'we have', c, 'times for the hour', hr