smallest = None
largest = None
count = 0
total = 0 
for num in [4, 5, 7, 8, 9, 10]:
	if smallest is None or num < smallest :
		smallest = num
	if largest is None or num > largest :
		largest = num 
   	count = count + 1
	total = total + num
print "the smallest is ", smallest
print "The largest is ", largest
print "number if iteration: ",  count 
print "sum of the numbers on the list ", total
print "average:  ", total / count



