#import unittest.TestCase() as test

def isLeapYear(year):
    #your code here. Try to do it in one line.
    return year % 4 == 0 and (not year % 100 == 0 or year % 400 == 0)
    
#describe('Leap years (should equal True)')
print str(isLeapYear(1984)) + ' True, Year 1984 was a leap year!'
print str(isLeapYear(2000)) + ' True, Year 2000 was a leap year!'

#describe('Normal years (should equal False)')
print str(isLeapYear(1234)) + ' False, Year 1234 was NOT a leap year!'
print str(isLeapYear(1100)) + ' False, Year 1100 was NOT a leap year!'