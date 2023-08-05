"""
Given an integer n, return the number of trailing zeroes in n!.

Full description:
https://leetcode.com/problems/factorial-trailing-zeroes/
"""
from math import factorial


# My solution
def trailing_zeroes(n: int) -> int:
    if n < 5:
        return 0

    product = factorial(n)

    # Mathematical solution
    zeroes = 0
    trail = product % 10
    while trail == 0:
        zeroes += 1
        product //= 10
        trail = product % 10

    # Convert to string solution
    # string = str(product)
    # i = len(string)-1
    # while i >= 0 and string[i] == '0':
    #     zeroes += 1
    #     i -= 1

    return zeroes


# Solution from LeetCode
def trailing_zeroes_2(n: int) -> int:
    if n < 5:
        return 0

    p = 0
    while n >= 5:
        n = n // 5
        p += n

    return p
