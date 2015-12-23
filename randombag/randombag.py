#https://www.reddit.com/r/dailyprogrammer/comments/3ofsyb/20151012_challenge_236_easy_random_bag_system/
from random import shuffle

def randomPieces(length):
    source = []
    out = ""
    for i in range(length):
        if not source:
            source = ["O", "I", "S", "Z", "L", "J", "T"]
            shuffle(source)
        out += source.pop()
    return out

def verify(pieces):
    for i in range(0, len(pieces), 7):
        chunk = pieces[i:i+7]
        if any(chunk.count(j) > 1 for j in set(chunk)):
            return False
    return True
    
pieces = randomPieces(50)
print pieces
print verify(pieces)