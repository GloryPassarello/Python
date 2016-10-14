hours=raw_input("Enter your hours working: ")
try:
	hr=int(hours)
	print "thanks"
except:
	hr=-1
	print "Please, insert your hours working in a numerical format"
	quit()
pay=raw_input("Please, type your pay for hours: ")
try:
	pay=int(pay)
	print "thanks"
except:
	pay=-1
	print "Please, insert your pay in a numerical format"
	quit()
	
if hr<=40:
	Payment=hr*pay
else :
	Payment=hr*pay+(hr-40)*1.5*pay

print "Your pay is in euro: ", Payment