"""
Given the head of a singly linked list, return true if it is a palindrome
or false otherwise.

Full description:
https://leetcode.com/problems/palindrome-linked-list/
"""


# Definition for singly-linked list, given in the problem.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# My solution
def is_palindrome(head: ListNode) -> bool:
    indexes = dict()
    i = 1

    while head:
        indexes[i] = head.val
        head = head.next
        i += 1

    start = 1
    end = i - 1

    while start <= end:
        if indexes[start] != indexes[end]:
            return False
        start += 1
        end -= 1

    return True


# Solution from LeetCode
# class Solution(object):
#
#     def isPalindrome(self, head):
#         # part 1: Find the middle node of the linked list
#         # Initialize the two pointers at the head of the list
#         slow, fast = head, head
#         # Iterate over the entire linked list, until the fast pointer reaches the end
#         # The fast pointer moves twice as fast as the slow pointer,
#         # so when fast reaches the end, slow will be at the middle
#         while (fast is not None) and (fast.next is not None):
#             # Move the two pointers,
#             # with the fast pointer moving twice as fast as the slow pointer
#             slow = slow.next
#             fast = fast.next.next
#
#         # part 2: Reverse the second half of the linked list
#         # At this point, the slow pointer is at the start of the second half
#         reversed_second_half = self.reverse_linked_list(slow)
#
#         # part 3: Compare the reversed second half with the first half
#         # If they are the same, then the linked list is a palindrome
#         palindrome = self.compare_two_halves(head, reversed_second_half)
#         # Return True if the linked list is a palindrome, else False
#         return palindrome
#
#
#     def reverse_linked_list(self, head):
#         # Initialize pointers for previous, next, and current nodes
#         prev = None
#         next = None
#         curr = head
#         # Iterate over the linked list, reversing the link between each pair of nodes
#         while curr is not None:
#             # Store the next node
#             next = curr.next
#             # Reverse the link to the previous node
#             curr.next = prev
#             # Move on to the next node
#             prev = curr
#             curr = next
#         # Return the head of the reversed linked list
#         return prev
#
#
#     def compare_two_halves(self, first_half, second_half):
#         # If any pair of nodes have different values,
#         # then the linked list is not a palindrome
#         while first_half and second_half:
#             if first_half.val != second_half.val:
#                 return False
#             else:
#                 first_half = first_half.next
#                 second_half = second_half.next
#         # If reach the end of either halves without finding any different values,
#         # then the linked list is a palindrome
#         return True
