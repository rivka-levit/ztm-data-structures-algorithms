"""
Reverse bits of a given 32 bits unsigned integer.

Full description:
https://leetcode.com/problems/reverse-bits/
"""


def reverse_bits(n: int) -> int:
    bin_n = str(format(n, 'b'))
    bin_n = '0' * (32 - len(bin_n)) + bin_n

    reversed_bin_n = '0b' + bin_n[::-1]

    return int(reversed_bin_n, 2)
