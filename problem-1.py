#!/usr/bin/env python

def main():
    '''Find the sum of all the multiples of 3 or 5 below 1000.'''
    print sum(filter(lambda x: x % 3 == 0 or x % 5 == 0, range(1000)))

if __name__ == '__main__':
    main()
