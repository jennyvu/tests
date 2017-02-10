#!/usr/bin/env python
import random
"""Guessing number in range 1 to 100
Player will try enter number until got correct number
"""

def guessing_try():
    print "Enter number from 1 to 100"
    randompick = random.randint(1, 100) # random pick number from 1 to 100

    found = False                   # flag
    try_times = 0
    while not found:
        inputnumber = input("Enber number: ")
        if inputnumber == randompick:
            print "You got it!"
            found = True
        elif inputnumber > randompick:
            print "Try with lower..."
        else:
            print "Try with higher..."
        try_times += 1

    # printing congrats
    print "Thank you for playing your are success after {0} trieves".\
        format(try_times)

if __name__ == '__main__':
    guessing_try()
