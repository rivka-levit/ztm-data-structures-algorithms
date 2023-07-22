"""
Given an integer array nums where the elements are sorted in ascending
order, convert it to a height-balanced binary search tree.

Full description:
https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
"""


# Definition for a binary tree node, given in the description.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def sorted_array_to_bst(nums: list[int]) -> TreeNode | None:
    if not nums:
        return None

    mid_ind = len(nums) // 2
    root = TreeNode(nums[mid_ind])

    root.left = sorted_array_to_bst(nums[: mid_ind])
    root.right = sorted_array_to_bst(nums[mid_ind+1:])

    return root
