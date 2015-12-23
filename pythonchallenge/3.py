# www.pythonchallenge.com/pc/def/equality.html

s = "".join([line.rstrip() for line in open('3.txt')])
o = ""

for i in range(4, len(s)-4):
    first = s[i-4]
    begin = s[i-3:i]
    char = s[i]
    end = s[i+1:i+4]
    last = s[i+4]
    if char.islower() and begin.isupper() and end.isupper() and first.islower() and last.islower():
        o += char

print o
