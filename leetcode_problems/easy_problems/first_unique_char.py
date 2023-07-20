"""
Given a string s, find the first non-repeating character in it
and return its index. If it does not exist, return -1.

Full description:
https://leetcode.com/problems/first-unique-character-in-a-string/
"""


# My solution
def first_unique_char(s: str) -> int:
    chars = dict()
    for ch in s:
        chars[ch] = chars.get(ch, 0) + 1

    chars = {k: v for k, v in chars.items() if v == 1}

    for i in range(len(s)):
        if s[i] in chars:
            return i
    return -1


# Solution from LeetCode:
# def first_unique_char(s: str) -> int:
#     chars = dict()
#     for i, ch in enumerate(s):
#         if ch in chars:
#             chars[ch] = -1
#         else:
#             chars[ch] = i
#
#     for i, ch in enumerate(s):
#         if chars[ch] != -1:
#             return i
#
#     return -1
