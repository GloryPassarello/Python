#fname = raw_input("Enter file name: ")
fh = open('/home/anabrs1/Python_material/code/romeo.txt')
#I will read the fh2 as a string
fh2 = fh.read()
lst = fh2.split()


for x in lst:
    if x in lst:
        lst.remove(x)
lst.sort()
print lst
print 'This code gives a wrong output: required debugging'