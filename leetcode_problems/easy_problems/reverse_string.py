"""
Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.

Full description:
https://leetcode.com/problems/reverse-string/description/
"""


def reverse_string(s: list):
    s[:] = s[::-1]

    # My first solution:

    # start = 0
    # end = len(s) - 1
    #
    # while start != end and end > start:
    #     s[start], s[end] = s[end], s[start]
    #     start += 1
    #     end -= 1
