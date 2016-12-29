file = open('regex_sum_316305.txt')
txt=file.read()
import re
m = re.findall('([0-9]+)', txt)
print sum([int(x) for x in m])