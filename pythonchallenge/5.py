# www.pythonchallenge.com/pc/def/peak.html

import pickle

with open("/storage/python/programs/pythonchallenge/banner.p", 'rb') as file:
    file = pickle.load(file)
    for line in file:
        templine = ''
        for each in line:
            for i in range(each[1]):
                 templine += each[0]
        print templine
        #print ''.join(c * n for c, n in line)
