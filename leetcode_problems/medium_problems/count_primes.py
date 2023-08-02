"""
Given an integer n, return the number of prime numbers
that are strictly less than n.

Full description:
https://leetcode.com/problems/count-primes/
"""


def count_primes(n: int) -> int:
    if n <= 1:
        return 0
    if n == 2:
        return 1

    primes = [True for _ in range(n)]

    mult = 2

    while mult * mult < n:

        if primes[mult] is True:
            for i in range(mult*mult, n, mult):
                primes[i] = False

        mult += 1

    return primes[2:].count(True)
