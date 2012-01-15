#!/usr/bin/env python

def fibonacci(max):
    '''The fibonacci sequence up to the value: max.'''
    a, b = 0, 1
    while a < max:
        a, b = b, a + b
        yield a # This method is a generator. ;)

def main():
    '''Find the sum of even-valued terms in the fibonacci sequence
    that do not exceed four million.'''
    print sum([x for x in fibonacci(4000000) if x % 2 == 0])

if __name__ == '__main__':
    main()
