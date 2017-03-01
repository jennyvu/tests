#!/usr/bin/env python

def xmastree(n):
    y = n - 1
    x = 1
    for i in range(n):
        print (' ' * y + '+' * x)
        x += 2
        y -= 1

if __name__ == '__main__':
    xmastree(6)
