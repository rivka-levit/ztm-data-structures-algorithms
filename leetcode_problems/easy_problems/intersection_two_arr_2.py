"""
Given two integer arrays nums1 and nums2, return an array
of their intersection. Each element in the result must appear
as many times as it shows in both arrays and you may return the
result in any order.

Full description:
https://leetcode.com/problems/intersection-of-two-arrays-ii/
"""


# My solution
def intersect(nums1: list[int], nums2: list[int]) -> list[int]:
    hash_nums_1 = dict()
    hash_nums_2 = dict()
    intersection = list()

    for i in nums1:
        hash_nums_1[i] = hash_nums_1.get(i, 0) + 1

    for i in nums2:
        hash_nums_2[i] = hash_nums_2.get(i, 0) + 1

    for i in hash_nums_1:
        if i in hash_nums_2:
            for _ in range(min(hash_nums_1[i], hash_nums_2[i])):
                intersection.append(i)

    return intersection


# Solution from LeetCode:
# def intersect(nums1: list[int], nums2: list[int]) -> list[int]:
#     nums1.sort()
#     nums2.sort()
#     ans = []
#     i = j = 0
#     while i < len(nums1) and j < len(nums2):
#         if nums1[i] < nums2[j]:
#             i += 1
#         elif nums1[i] > nums2[j]:
#             j += 1
#         else:
#             ans.append(nums1[i])
#             i += 1
#             j += 1
#     return ans
