"""
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times.
You may assume that the majority element always exists in the array.

Full description:
https://leetcode.com/problems/majority-element/
"""


# My solution
def majority_element(nums: list) -> int:
    majority = 0
    element = None
    hash_nums = dict()

    for n in nums:
        hash_nums[n] = hash_nums.get(n, 0) + 1
        if hash_nums[n] > majority:
            element = n
            majority = hash_nums[n]

    return element


# Solution from LeetCode
# def majority_element(nums: list) -> int:
#     nums.sort()
#     return nums[int(len(nums)/2)]
