letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'l']
numbers = [1, 2, 3, 5, 8, 9, 8, 56,7 ,8 ,9, 8, 7, 10, 12, 56, 84]

def chop(t):  
  del t[0]    
  del t[len(t)-1]    

lets = chop(letters)

print letters
print lets

def middle(t):  
  t2 = t[1:-1]  
  return t2  

mid_numbers=middle(numbers)
print mid_numbers
print numbers