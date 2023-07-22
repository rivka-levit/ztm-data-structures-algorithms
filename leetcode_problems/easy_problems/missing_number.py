"""
Given an array nums containing n distinct numbers in the range [0, n],
return the only number in the range that is missing from the array.

Full description:
https://leetcode.com/problems/missing-number/
"""


# O(1) space complexity
def missing_number(nums: list[int]) -> int:
    nums.sort()
    n = len(nums)
    for i in range(n):
        if i != nums[i]:
            return i
    return n


# O(n) space complexity, but faster
def missing_number_2(nums: list[int]) -> int:
    nums = set(nums)
    for i in range(len(nums) + 1):
        if i not in nums:
            return i


# Solution from LeetCode
# def missing_number(nums):
#     return sum(range(len(nums) + 1)) - sum(nums)
