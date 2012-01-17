#!/usr/bin/env python

def main():
    '''Find the difference between the sum of the squares of the first
    one hundred natural numbers and the square of the sum'''
    sum_of_squares = sum([(i + 1) * (i + 1) for i in xrange(100)])
    square_of_sum  = sum([i + 1 for i in xrange(100)]) * sum([i + 1 for i in
        xrange(100)])
    print square_of_sum - sum_of_squares

if __name__ == '__main__':
    main()
