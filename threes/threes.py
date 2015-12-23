def playThrees(input):
    if input == 1:
        print input
        
    elif input % 3 == 0:
        print str(input) + '\t 0'
        playThrees(input/3)
    
    elif input % 3 == 1:
        print str(input) + '\t-1'
        playThrees((input-1)/3)
        
    else:
        print str(input) + '\t+1'
        playThrees((input+1)/3)

while True:
    try:
        input = int(raw_input("Enter an integer: "))
        break
    except ValueError:
        print "Oops!  That was not an integer.  Try again..."

playThrees(input)