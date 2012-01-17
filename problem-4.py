#!/usr/bin/env python

def is_palindrome(number):
    return str(number) == str(number)[::-1]

def main():
    '''Find the largest palindrome made from the product of two
    three-digit numbers.'''
    palindromes = []
    for x in xrange(1000, 100, -1):
        for y in xrange(1000, 100, -1):
            product = x*y
            is_pal = is_palindrome(product)
            if is_pal:
                palindromes.append((str(x) + 'x' + str(y), product))
    # That got out all palindromes in between 100 and 999
    # including some duplicates, so...
    print max(palindromes, key=lambda x: x[1])

if __name__ == '__main__':
    main()
