# www.pythongchallenge.com/pc/def/ocr.html

i = "".join([line.rstrip() for line in open('2.txt')])
i.lower()
o = ""

for char in i:
    if ((ord(char)>=97) and (ord(char)<=122)):
        o += char
print o

