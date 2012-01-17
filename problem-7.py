#!/usr/bin/env python

def is_prime(x):
    if x <= 1:
        return False

    for i in xrange(2, x):
        if x % i == 0:
            return False

    return True

def main():
    '''What is the 10001st prime number?'''
    prime_index = 1
    i = 1
    while prime_index <= 10001:
        if is_prime(i):
            if prime_index == 10001:
                print "%s: %s is a prime number" % (str(prime_index), str(i))
            prime_index += 1
        i += 1

if __name__ == '__main__':
    main()
