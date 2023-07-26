"""
Given an array of integers nums and an integer target, return indices
of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution,
and you may not use the same element twice.

You can return the answer in any order.

Full description:
https://leetcode.com/problems/two-sum/
"""


def two_sum(nums: list[int], target: int) -> list:
    visited = dict()

    for i in range(len(nums)):
        compliment = target - nums[i]
        if compliment in visited:
            return [visited[compliment], i]
        visited[nums[i]] = i
