# http://www.pythonchallenge.com/pc/def/oxygen.html

import Image

im = Image.open("oxygen.png")

o = ''
w, h = im.size
#print w, h
for i in range(0, 605, 7):
    o += chr(im.getpixel((i, h/2))[0])

print o
