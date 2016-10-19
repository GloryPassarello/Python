def count(imp):
	count=0
	for letter in imp:
		if letter == 'a':
			count=count +1
	print 'The a you wrote are', count


name = raw_input('Please, enter your name: ')

count(name)