str = 'X-DSPAM-Confidence: 0.8475'
colon=str.find(':') + 1 #python always starts with 0 every line
number= str[colon:]
number.lstrip()
number=float(number) #remember to alwas rename a variable 
print number
print type(number)