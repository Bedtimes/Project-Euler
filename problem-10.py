#!/usr/bin/env python

def primes_sieve(limit):
    # http://stackoverflow.com/questions/3939660/sieve-of-eratosthenes-finding-primes-python
    a = [True] * limit                          # Initialize the primality list
    a[0] = a[1] = False

    for (i, isprime) in enumerate(a):
        if isprime:
            yield i
            for n in xrange(i*i, limit, i):     # Mark factors non-prime
                a[n] = False

def main():
    '''Find the sum of all the primes below 2 million.'''
    primes = [i for i in primes_sieve(2000000)]
    print sum(primes)

if __name__ == '__main__':
    main()
