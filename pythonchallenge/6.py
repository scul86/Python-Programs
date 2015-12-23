# www.pythonchallenge.com/pc/def/channel.html

from zipfile import ZipFile

c, f, e = [], "90052", ".txt"

with ZipFile("channel.zip") as file:
    while True:
        path = f + e
        line = file.read(path)
        c.append(file.getinfo(path).comment)
        if not line[:4] == "Next":
            break
        f = line.split()[-1]

print "".join(c)
