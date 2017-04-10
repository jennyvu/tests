#!/usr/bin/env python

"""
write program take the number from 1 to 100 and print out multiple or 3 prints
'Fizz' if multiple by 3, 'Buzz' if multiple by 5, and FizzBuzz if multiple
with both 3 and 5
"""

def print_fizzbuzz():
    for x in range(1,100):
        if x % 15 == 0:
            print 'FixxBuzz'
        elif x % 3 == 0:
            print 'Fixx'
        elif x % 5 == 0:
            print 'Buzz'
        else:
            print x

if __name__ == '__main__':
    print_fizzbuzz()