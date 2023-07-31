"""
Given the heads of two singly linked-lists headA and headB, return the node
at which the two lists intersect. If the two linked lists have no intersection
at all, return null.

Full description:
https://leetcode.com/problems/intersection-of-two-linked-lists/
"""


# Definition for singly-linked list, given in the problem.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def get_intersection_node(headA: ListNode, headB: ListNode) -> ListNode | None:
    intersect = None
    visited = set()

    while headA:
        visited.add(headA)
        headA = headA.next

    while headB:
        if headB in visited:
            intersect = headB
            break
        headB = headB.next

    return intersect
