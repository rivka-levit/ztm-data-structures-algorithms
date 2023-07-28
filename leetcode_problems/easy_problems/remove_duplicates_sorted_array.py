"""
Given an integer array nums sorted in non-decreasing order,
remove the duplicates in-place such that each unique element
appears only once. The relative order of the elements should be kept
the same. Then return the number of unique elements in nums.

Full description:
https://leetcode.com/problems/remove-duplicates-from-sorted-array/
"""


def remove_duplicates(nums: list[int]) -> int:
    i = 0

    for n in nums:
        if n != nums[i]:
            i += 1
            nums[i] = n

    return i + 1
