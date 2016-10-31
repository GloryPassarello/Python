letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'l']
numbers = [1, 2, 3, 5, 8, 9, 8, 56,7 ,8 ,9, 8, 7, 10, 12, 56, 84]

def chop(t):
	del t[0]
	del t[len(t)-1]
	#correct use of the function is call the function and then print the results of the function
	#otherwise i will obtein the return value by default, None. 
chop(letters)
print letters

#I can obtain the same with the function below:

def chop(t):  
  del t[0]    
  del t[len(t)-1]    
  return t 
print chop(letters)

def middle(t):
	t2 = t[1:-1]
	return t2

print middle(numbers)

