import random

class not_cv(Exception):
    pass
    
def randWord(list):
    c, v = "bcdfghjklmnpqrstvwxyz", "aeiouy"

    output = ''

    for char in list:
        if char.lower() not in 'cv':
            raise not_cv
        elif char == 'c':
            output += random.choice(c)
        elif char == 'C':
            output += random.choice(c).upper()
        elif char == 'v':
            output += random.choice(v)
        else:
            output += random.choice(v).upper()
            
    return output

while True:    
    try:
        input = raw_input("Enter a string of C & V: ")
        o = randWord(input)
        print o
        break
    except not_cv:
        print "Enter a string with only Cs and/or Vs"