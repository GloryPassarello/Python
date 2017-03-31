##how to use a function:
#defining a function

def square_numbers(num):
    result = [] ##to be defined inside the function
    for x in num:
        result.append(x**2)
    return result
##alone this function not run
##I need to define the number I want to use
##return can be used by another function
my_list = [1, 2, 3, 25 ,5 ,8, 7, 8, 9, 10]
my_list2 = range(250)
print 'you are using a def function', square_numbers(my_list)
#print square_numbers(my_list2)


####GENERATORS####
#with a generator I don't need to define a list anymore
#and I don't need to return the list anymore
def square_numbers_generator(num):
    for x in num:
        yield x**2

print 'you are using generator now..'
print square_numbers_generator(my_list)
print 'you have back a generator object: generators gives you back objects in memory'
print 'generators have implemented next()'
#generators don't hold the entire results in memory. it is asking you the next results

output = square_numbers_generator(my_list)
print 'using next()'
print next(output)
#each time I print next I go to the next one
print next(output), 'printing the next..'
print next(output)
print next(output)
print next(output)
print next(output)
print next(output)
#print next(output)
#print next(output)
#print next(output)
##I am automatizing the next() I am  not builting a new one.
for nums in output:
    print 'making a test ', nums



#for that reason generators are used with for loop
print 'using generator with for loop: we need to create another object using the function'
print 'Python already gives you back the output of yield that is built with next'
output2 = square_numbers_generator(my_list)
for nums in output2:
    print nums
#no error: for loop know when to stop

##list comprehesion###
print '========================================='
print 'we can do the same with list comprehesion'
comprehesion_list = [x**2 for x in my_list]
print comprehesion_list
print [x**2 for x in my_list]
print list(x**2 for x in my_list)
print (x**2 for x in my_list)
