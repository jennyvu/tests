#!/usr/bin/env python

def fib(n):
   if n == 1:
      return 1
   elif n == 0:
      return 0
   else:
      return fib(n-1) + fib(n-2)

def fibonacci_sequence(n):
    for i in range(n + 1):
        print fib(i)

if  __name__ == '__main__':
    fibonacci_sequence(5)