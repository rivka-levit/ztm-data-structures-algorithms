"""
Given an integer array nums, return true if any value appears at least
twice in the array, and return false if every element is distinct.

Full description:
https://leetcode.com/problems/contains-duplicate/
"""


# My solution
def contains_duplicate(nums: list[int]) -> bool:
    uniques = set()

    for n in nums:
        if n in uniques:
            return True
        uniques.add(n)

    return False


# Solution from LeetCode
# def contains_duplicate(nums: list[int]) -> bool:
#     sorted_list = sorted(nums)
#
#     for i in range(len(nums) - 1):
#         if sorted_list[i] == sorted_list[i + 1]:
#             return True
#
#     return False
