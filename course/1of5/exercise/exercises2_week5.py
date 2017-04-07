try:
    number=raw_input("Type a number between 0 and 10: ")
    number=int(number) 
    if number >= 8:
        print "Cool"
    elif number >= 6:
        print "Good"
    elif number >= 4:
        print "Meh"
        print "Good"

elif number >= 2:
    print "Nevermind"
elif number <=0:
    print "Ouch!"
print "Well done"
except:
    print "pleace, write a number"




