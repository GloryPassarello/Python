num = range(35) #RANGE GIVES YOU BACK A LIST

results = filter(lambda x: x%2, num)
results_map = map (lambda x : x**3, num)


print 'i am appling filter'
print results

print 'i am appling map with if'
print results_map
