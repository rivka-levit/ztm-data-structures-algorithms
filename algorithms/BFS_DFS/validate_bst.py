from collections import deque


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# My solution that didn't pass all the tests
class Solution(object):
    def isValidBST(self, root: TreeNode) -> bool:
        """
        :type root: TreeNode
        :rtype: bool
        """

        def lookup(value):
            temp = root
            while temp:
                if value == temp.value:
                    return temp
                if value > temp.value:
                    temp = temp.right
                else:
                    temp = temp.left
            return None

        conditions = (
            isinstance(root, TreeNode),
            root.left is None or root.left.val < root.val,
            root.right is None or root.right.val > root.val
        )

        q = deque()
        q.append(root)

        while q:
            current = q.popleft()
            if not all(conditions):
                return False
            if not lookup(current.val):
                return False
            if current.left:
                q.append(current.left)
            if current.right:
                q.append(current.right)

        return True


# Right solution
class Solution(object):
    def isValidBST(self, root: TreeNode) -> bool:
        """
        :type root: TreeNode
        :rtype: bool
        """

        def helper(node, low, high):
            if not node:
                return True
            if not low < node.val < high:
                return False
            return helper(node.left, low, node.val) and helper(node.right, node.val, high)

        return helper(root, float('-inf'), float('inf'))
