"""
Given an integer n, return true if it is a power of three.
Otherwise, return false.

An integer n is a power of three, if there exists an integer x such that n == 3x.

Full description:
https://leetcode.com/problems/power-of-three/
"""
from math import log


def is_power_of_three(n: int) -> bool:
    if n <= 0:
        return False

    x = round(log(n, 3))
    return 3 ** x == n
