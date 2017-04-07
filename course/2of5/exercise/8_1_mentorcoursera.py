letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'l']
numbers = [1, 2, 3, 5, 8, 9, 8, 56,7 ,8 ,9, 8, 7, 10, 12, 56, 84]

def chop(t):
    del t[0]
    del t[len(t)-1]

print "letters list before chop()", letters
letter = chop(letters)
print "letters list after chop()", letters
print "letters list after chop()", letter

def middle(t):
    t2 = t[1:-1]
    #return t2

print
print "numbers list before middle()", numbers
mid_numbers = middle(numbers)
print "numbers list after middle()", numbers
print "new list made from numbers", mid_numbers
