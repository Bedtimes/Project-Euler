#!/usr/bin/env python

def main():
    '''What is the smallest positive number that is evenly
    divisible by all of then numbers from 1 to 20'''
    i = 2520
    while i >= 2520:
        for j in range(11, 21):
            if i % j != 0:
                break
            if j == 20:
                print i
                return
        i += 2520

if __name__ == '__main__':
    main()
