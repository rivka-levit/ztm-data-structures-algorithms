"""
Given the root of a binary tree, return the inorder traversal
of its nodes' values.

Full description:
https://leetcode.com/problems/binary-tree-inorder-traversal/
"""


# Definition for a binary tree node, given in the problem.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inorder_traversal(root: TreeNode, v=None) -> list[int] | None:
    if not root:
        return

    if v is None:
        v = list()

    inorder_traversal(root.left, v=v)
    v.append(root.val)
    inorder_traversal(root.right, v=v)

    return v


