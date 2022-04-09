# Author: Anurag Lodhi | April 9, 2022 22:47
# Uses Euclid's algorithm to find the Greatest Common Divisor of two numbers

def GCD(a, b):
    if b > a:
        a, b = b, a
    while 1:
        a1 = a
        b1 = b
        a = b1
        b = a1 % b1
        if b == 0:
            return b1
