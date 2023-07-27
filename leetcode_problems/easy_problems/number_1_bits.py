"""
Write a function that takes the binary representation of an unsigned integer
and returns the number of '1' bits it has (also known as the Hamming weight).

Full description:
https://leetcode.com/problems/number-of-1-bits/
"""


# Arithmetical solution
def hamming_weight(n: int) -> int:
    result = 0
    n = int(format(n, 'b'))

    while n:
        last_num = n % 10

        if last_num == 1:
            result += 1

        n //= 10

    return result


# Solution with string
def hw(n):
    n = format(n, 'b')
    return n.count('1')
