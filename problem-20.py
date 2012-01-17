#!/usr/bin/env python

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def main():
    '''Find the sum of the digits in the number 100!'''
    print sum([int(i) for i in str(factorial(100))])

if __name__ == '__main__':
    main()
