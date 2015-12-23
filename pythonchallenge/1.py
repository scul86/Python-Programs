# www.pythonchallenge.com/pc/def/map.html

txt = "map"
changed = ""
for char in txt:
    if ((ord(char)>=97) and (ord(char)<=122)):
        trans = ord(char)+2
        if trans > 122:
            trans -= 26
        changed += chr(trans)
    else:
        changed += char
print changed
