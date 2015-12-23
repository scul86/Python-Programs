# www.pythonchallenge.com/pc/def/linkedlist.html

import urllib, string

count = 0
n = ''
last = raw_input("Enter Start: ")
for i in range(400):
    prev = n
    url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%s" %(last)
    n = urllib.urlopen(url).read()
    last = n.split()[-1]
    if not last.isdigit():
        print "\nPrev line: ", prev, "\nCurr line: ", n, "\n"
        new = raw_input("Enter new num? (Y/n): ")
        if new.lower() == 'n':
            break
        else:
            last = raw_input("new number: ")
    count += 1
print count
