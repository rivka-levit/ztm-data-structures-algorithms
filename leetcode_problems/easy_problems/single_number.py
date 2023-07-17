"""
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

Full description:
https://leetcode.com/problems/single-number/description/
"""


def single_number(nums: list) -> int:
    counted = set()

    for n in nums:
        if n in counted:
            counted.remove(n)
        else:
            counted.add(n)

    return [i for i in counted][0]
