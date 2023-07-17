"""
There is a singly-linked list head, and we want to delete a node in it.

Full description:
https://leetcode.com/problems/delete-node-in-a-linked-list/
"""


class ListNode(object):
    # Definition for singly-linked list given in the problem.
    def __init__(self, x):
        self.val = x
        self.next = None


def delete_node(node: ListNode) -> None:
    node.val, node.next.val = node.next.val, node.val
    node.next = node.next.next
