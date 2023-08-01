"""
Given an integer array nums, rotate the array to the right by k steps,
where k is non-negative.

Full description:
https://leetcode.com/problems/rotate-array/
"""


def rotate_1(nums: list[int], k: int) -> None:
    k %= len(nums)
    nums[:] = nums[-k:] + nums[:-k]
