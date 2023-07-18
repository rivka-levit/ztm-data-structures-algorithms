"""
Given the head of a singly linked list, reverse the list,
and return the reversed list.

Full description:
https://leetcode.com/problems/reverse-linked-list/
"""


# Definition for singly-linked list, given in the problem.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_ll(head: ListNode) -> ListNode:
    before = None
    current = after = head

    while after:
        after = after.next
        current.next = before
        before = current
        current = after

    head = before

    return head
