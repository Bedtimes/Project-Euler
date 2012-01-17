#!/usr/bin/env python
from operator import mul
from functools import reduce

def main():
    f = open('./problem-8.digits', 'r')
    digit_string = f.read().strip()
    digit_array = [int(i) for i in digit_string]

    highest_product = ([0, 0, 0, 0, 0], 0)
    i = 0
    while i < len(digit_array):
        if i <= 995:
            digits = digit_array[i : i + 5]
            temp_product = reduce(mul, digits)
            # print "%s => %s" % (digits, temp_product)
            if highest_product[1] < temp_product:
                highest_product = (digits, temp_product)

        i += 1
    print "%s => %s" % highest_product

if __name__ == '__main__':
    main()
