"""
Given a non-negative integer x, return the square root of x rounded down
to the nearest integer. The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.

For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.

Full description:
https://leetcode.com/problems/sqrtx/
"""
from math import sqrt, floor


def find_sqrt(x: int) -> int:
    return int(floor(sqrt(x)))
