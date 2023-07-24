"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made
by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

Full description:
https://leetcode.com/problems/merge-two-sorted-lists/
"""


# Definition for singly-linked list, given in the description.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# My solution
def merge_sorted_ll(list1: ListNode, list2: ListNode) -> ListNode | None:
    if not list1 and not list2:
        return None
    if not list1:
        return list2
    if not list2:
        return list1

    dummy = temp = ListNode(val=0)

    while list1 and list2:
        if list1.val < list2.val:
            temp.next = list1
            list1 = list1.next
        else:
            temp.next = list2
            list2 = list2.next

        temp = temp.next

    if list1:
        temp.next = list1
    if list2:
        temp.next = list2

    return dummy.next


# Solution from LeetCode
# def merge_sorted_ll(list1: ListNode, list2: ListNode) -> ListNode | None:
#     dummy = temp = ListNode(0)
#     while list1 != None and list2 != None:  # 1
#
#         if list1.val < list2.val:  # 2
#             temp.next = list1  # 3
#             list1 = list1.next  # 4
#         else:
#             temp.next = list2
#             list2 = list2.next
#         temp = temp.next
#     temp.next = list1 or list2  # 5
#     return dummy.next  # 6
