#!/usr/bin/env python3
import math

class Multiplier:
    def multiply(a,b):
        n = len(str(a))
        n2 = len(str(b))
        if n ==1 and n2 ==1:
            return a*b
        a_half1 = math.floor(a/(10**(n/2)))
        a_half2 = a%(10**(n/2))
        b_half1 = math.floor(b/(10**(n/2)))
        b_half2 = b%(10**(n/2))
        ac = multiply(a_half1,b_half1)
        bd = multiply(a_half2,b_half2)
        sun = multiply((a_half1 + a_half2), (b_half1+b_half2)) - ac - bd
        return (10**n)*ac + (10**(n/2))*sun + bd


print(Multiplier.multiply(3,5))