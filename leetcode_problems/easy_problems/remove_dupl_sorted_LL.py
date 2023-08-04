"""
Given the head of a sorted linked list, delete all duplicates such that
each element appears only once. Return the linked list sorted as well.

Full description:
https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# My solution
def remove_duplicates(head: ListNode) -> ListNode:
    if not head or not head.next:
        return head

    # Create set with uniques values and add the first value
    uniques = {head.val}

    prev = head
    current = head.next

    while current:
        if current.val in uniques:
            prev.next = current.next
        else:
            uniques.add(current.val)
            prev = prev.next

        current = current.next

    return head


# Solution from LeetCode
# def remove_duplicates(head: ListNode) -> ListNode:
#     current = head
#     while current:
#         while current.next and current.val == current.next.val:
#             current.next = current.next.next
#         current = current.next
#     return head
