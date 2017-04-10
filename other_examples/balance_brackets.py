#!/usr/bin/env python

def is_matched(expression):
    brackets = '{}[]()'
    match = True
    stack = []
    exp_len = len(expression)
    if exp_len % 2 != 0:
        match = False
    elif exp_len < 2 or exp_len > 1000:
        match = False
    else:
        for i in xrange(exp_len):
            br = expression[i]
            if is_open_br(br):
                stack.append(br)
            elif is_close_br(br):
                if len(stack) > 0 and match_br(stack[len(stack) - 1], br):
                    stack.pop()
                else:
                    match = False
            else:
                match = False

    if len(stack) != 0:
        match = False

    return match

def is_open_br(br):
    if br == '{' or br == '[' or br == '(':
        return True
    else:
        return False

def is_close_br(br):
    if br == '}' or br == ']' or br == ')':
        return True
    else:
        return False

def match_br(a, b):
    if a == '{' and b == '}':
        return True
    if a == '[' and b == ']':
        return True
    if a == '(' and b == ')':
        return True
    else:
        return False

if  __name__ == '__main__':
    t = 3
    for a0 in xrange(t):
        expression = raw_input().strip()
        if is_matched(expression) == True:
            print "YES"
        else:
            print "NO"