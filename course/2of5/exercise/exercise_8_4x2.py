#this script will generate a list of no repeated word inside the input text 

fh = open('/home/anabrs1/Python_material/code/romeo.txt')
fh2 = fh.read()
#lst_list = list(fh2) not really usefull
lst = fh2.split() # split return a list 
t=list() #creating a new empty list 
for x in lst:
    if x not in t:
        t.append(x)
t.sort()
print t

    
