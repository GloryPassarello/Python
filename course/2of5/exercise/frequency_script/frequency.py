file = raw_input('Please, inser a file text:')
if len(file) < 1 : file = 'english.txt'
txt = open (file)
inp=txt.read()
inp2=inp.lower()
ist=dict()
#counting the letter present on the file
for l in inp2:
	ist[l]=ist.get(l,0) +1
#creating a list made by the alphabet
import string
alpha = list(string.lowercase[:])
#note: if the dictionary change, RuntimeError: dictionary changed size during iteration accurs 
for key in list(ist): #it is necessary list() to avoid run time error
	if key not in alpha:
		del ist[key]
#print ist
summ=float(sum(ist.values()))
#print summ

#for v in ist.values():
#	perc =float(v)/summ*100
#	print perc

sorted_list=list()
for k, v in ist.items():
	v =float(v)/summ*100
	sorted_list.append((v,k))
sorted_list.sort(reverse=True)
#print sorted_list
#percentage, lett = sorted_list
for element in sorted_list:
	print element