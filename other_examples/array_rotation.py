#!/usr/bin/env python

def array_left_rotation(a, n, k):
    for i in range(1, k+1):
        first = a[0]
        for j in range(0, n-1):
            a[j] = a[j + 1]
        a[n-1] = first
    return a

if  __name__ == '__main__':
    array = array_left_rotation([1,2,3,4,5], 5, 4)
    print array