"""
Given a signed 32-bit integer x, return x with its digits reversed.
If reversing x causes the value to go outside the signed 32-bit integer
range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers
(signed or unsigned).

Full description:
https://leetcode.com/problems/reverse-integer/description/
"""


def reverse_integer(x: int) -> int:
    rev = str(x)[::-1]
    sign = ''

    if rev[-1] == '-':
        sign = '-'
        rev = rev[:-1]

    if int(rev) > 2 ** 31 - 1:
        return 0

    return int(sign + rev)
