#!/usr/bin/env python
from math import sqrt
from sets import Set

max_integer = 600851475143

def is_prime(x):
    if x <= 1:
        return False

    for i in xrange(2, x):
        if x % i == 0:
            return False

    return True

def main():
    '''The largest prime factor of the number 600851475143'''
    prime_factors = Set()
    for i in xrange(1, int(sqrt(max_integer))):
        if max_integer % i == 0 and is_prime(i):
            prime_factors.add(i)
    print max(prime_factors)

if __name__ == '__main__':
    main()
