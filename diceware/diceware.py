from random import randint

class Diceware:
    __dict = {}
    
    def __init__(self):
        f = open('dicewarewordlist.txt', 'r')
        for line in f:
            s = line.split()
            self.__dict[s[0]] = s[1]
        f.close()

    def run(self, l):
        for i in range(l):
            e, val = 1, 0
            for j in range(5):
                r = randint(1, 6)
                r *= e # *= (1, 10, 100, 1000, etc)
                val += r
                e *= 10
            print self.__dict[str(val)],
        val = None
        
while True:
    try:
        num = int(raw_input("How many words: "))
        break
    except ValueError:
        print "Oops!  That was not an integer.  Try again..."

d = Diceware()
d.run(num)
