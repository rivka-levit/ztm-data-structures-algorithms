"""
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order,
and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored
inside the array nums1. To accommodate this, nums1 has a length of m + n, where the
first m elements denote the elements that should be merged, and the last n elements
are set to 0 and should be ignored. nums2 has a length of n.

Full description:
https://leetcode.com/problems/merge-sorted-array/description/
"""


def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    if not m:
        nums1[:] = nums2
        return

    i = m + n - 1
    m -= 1
    n -= 1

    while n >= 0:
        if m < 0 or nums2[n] > nums1[m]:
            nums1[i] = nums2[n]
            i -= 1
            n -= 1
        else:
            nums1[i] = nums1[m]
            i -= 1
            m -= 1
