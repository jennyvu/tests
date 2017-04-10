#!/usr/bin/env python

def number_needed(a, b):
    no_delete = 0
    for i in xrange(len(a)):
        if a[i] not in b:
            a.strip(a[i])
            no_delete += 1
    for i in xrange(len(b)):
        if b[i] not in a:
            b.strip(b[i])
            no_delete += 1
    return no_delete

if  __name__ == '__main__':
    print number_needed("abc", "cde")