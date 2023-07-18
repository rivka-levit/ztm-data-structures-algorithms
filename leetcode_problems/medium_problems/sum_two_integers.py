"""
Given two integers a and b, return the sum of the two integers
without using the operators + and -.

Full description:
https://leetcode.com/problems/sum-of-two-integers/description/
"""
import math


# First variant
def sum_two_int(a, b):
    if a == 0:
        return b
    elif b == 0:
        return a
    else:
        return int(math.log10(math.pow(10, a) * math.pow(10, b)))


# Second variant
def sum_two_int_2(a, b):
    return sum((a, b))
