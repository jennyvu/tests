#!/usr/bin/env python

def find_max(list = []):
    if list:
        largest = list[0]
        for i in range(1, len(list)):
            if largest < list[i]:
                largest = list[i]
        return largest
    else:
        return None

if __name__ == '__main__':
    mylist = [3,5,7,9,11,4,10]
    print find_max(mylist)
