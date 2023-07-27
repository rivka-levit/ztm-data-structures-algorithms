"""
Given the root of a binary tree, check whether it is a mirror of itself
(i.e., symmetric around its center).

Full description:
https://leetcode.com/problems/symmetric-tree/
"""
from collections import deque


# Definition for a binary tree node, given in the problem.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_symmetric(root: TreeNode) -> bool:
    queue_1 = deque([root])
    queue_2 = deque([root])

    while queue_1 and queue_2:
        pointer_1 = queue_1.popleft()
        pointer_2 = queue_2.pop()

        if not pointer_1 and not pointer_2:
            continue
        if not pointer_1 or not pointer_2:
            return False
        if pointer_1.val != pointer_2.val:
            return False

        queue_1.append(pointer_1.left)
        queue_1.append(pointer_1.right)

        queue_2.appendleft(pointer_2.right)
        queue_2.appendleft(pointer_2.left)

    return False if queue_1 or queue_2 else True
