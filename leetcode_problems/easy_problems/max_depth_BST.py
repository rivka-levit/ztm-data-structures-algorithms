"""
Given the root of a binary tree, return its maximum depth.

Full description:
https://leetcode.com/problems/maximum-depth-of-binary-tree/
"""


# Definition for a binary tree node, given in the description.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Solution
def max_depth(root: TreeNode, depth=0) -> int | None:
    if not root:
        return depth

    depth += 1
    left_depth = max_depth(root.left, depth)
    right_depth = max_depth(root.right, depth)

    return max(left_depth, right_depth)
