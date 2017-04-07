text=open("mbox.txt")
txt=text.read()
import re
m = re.findall('N.+?: ([0-9.]+)', txt)
#average = sum(m)/len(m)
s=float()
for x in m:
	num = float(x)
	s=s+num
average = s/len(m)
print average