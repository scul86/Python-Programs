import sys

cells = []

for x in range(0, 9):
    cells.append(str(x+1))

def printBoard():
    print '\n -----'
    print '|' + cells[0] + '|' + cells[1] + '|' + cells[2] + '|'
    print ' -----'
    print '|' + cells[3] + '|' + cells[4] + '|' + cells[5] + '|'
    print ' -----'
    print '|' + cells[6] + '|' + cells[7] + '|' + cells[8] + '|'
    print ' -----\n'

printBoard()
