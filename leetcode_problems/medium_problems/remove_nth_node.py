"""
Medium problem.
https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/

Given the head of a linked list, remove the nth node from the end of the list and return its head.

Example 1:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Example 2:
Input: head = [1], n = 1
Output: []

Example 3:
Input: head = [1,2], n = 1
Output: [1]

"""


class ListNode:
    # The Node class given in the conditions of the problem
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def remove_nth_from_end(head: ListNode, n: int):
    # Check edge cases
    if not head:
        return head
    if head.next is None and n == 1:
        head = None
        return head

    temp = prev = endpoint = head

    # Make the right distance between the node and the end of the list
    for _ in range(n):
        endpoint = endpoint.next

    # Remove the first item if it is the target found
    if endpoint is None:
        head = head.next
        return head

    # Move the pointers till the endpoint is really at the end of the list
    while endpoint:
        prev = temp
        temp = temp.next
        endpoint = endpoint.next

    # Remove the target node
    prev.next = temp.next

    return head
