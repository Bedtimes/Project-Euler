#!/usr/bin/env python
from math import sqrt
from operator import mul
from functools import reduce

def main():
    '''Find the product of the pythagorean triplet where a + b + c = 1000'''
    for a in xrange(500):
        for b in xrange(500):
            c = sqrt(a*a + b*b)
            if a + b + c == 1000:
                print "(%d, %d, %d) => abc => %d" % (a, b, c, reduce(mul, [a, b, c]))
                return

if __name__ == '__main__':
    main()
