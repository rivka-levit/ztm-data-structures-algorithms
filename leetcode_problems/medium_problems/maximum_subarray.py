"""
Given an integer array nums, find the subarray with the largest sum,
and return its sum.

Full description:
https://leetcode.com/problems/maximum-subarray/
"""


def max_subarray(nums: list[int]) -> int:
    largest_sum = float('-inf')
    current_sum = 0

    for n in nums:
        current_sum += n

        if n > current_sum:
            current_sum = n

        if current_sum > largest_sum:
            largest_sum = current_sum

    return largest_sum
