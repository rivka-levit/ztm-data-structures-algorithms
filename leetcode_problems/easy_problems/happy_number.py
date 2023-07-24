"""
Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum
of the squares of its digits.

Repeat the process until the number equals 1 (where it will stay),
or it loops endlessly in a cycle which does not include 1.

Those numbers for which this process ends in 1 are happy.

Return true if n is a happy number, and false if not.

Full description:
https://leetcode.com/problems/happy-number/
"""


def sum_squares(num: int) -> int:
    current_sum = 0
    while num:
        last_num = num % 10
        current_sum += last_num ** 2
        num //= 10
    return current_sum


def is_happy(n: int) -> bool:
    results = set()

    while n != 1:
        n = sum_squares(n)
        if n in results:
            return False
        results.add(n)

    return True
