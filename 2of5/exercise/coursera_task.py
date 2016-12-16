name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
hours=list()
for line in handle:
	if line.startswith('From '):
		d=line.split()
		h=d[5].split(':')
		hours.append(h[0])
ist=dict()
for x in hours:
	ist[x]=ist.get(x, 0)+1
l=list()
for k, v in ist.items():
	l.append((k, v))
l.sort()
for k, v in l:
	print k, v