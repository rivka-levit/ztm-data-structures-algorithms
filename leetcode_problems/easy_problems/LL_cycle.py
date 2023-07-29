"""
Given head, the head of a linked list, determine if the linked list has a cycle in it.

Full description:
https://leetcode.com/problems/linked-list-cycle/description/
"""


# Definition for singly-linked list, given in the description.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


# My solution with bad space complexity
def has_cycle(head: ListNode):
    nodes = set()

    while head:
        nodes.add(head)

        if head.next in nodes:
            return True

        head = head.next

    return False


# Solution from LeetCode
# def has_cycle(head: ListNode):
#     slow, fast = head, head
#
#     while fast and fast.next:
#         slow = slow.next
#         fast = fast.next.next
#         if slow == fast:
#             return True
#
#     return False
