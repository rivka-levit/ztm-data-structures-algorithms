"""
Given two strings needle and haystack, return the index of the first
occurrence of needle in haystack, or -1 if needle is not part of haystack.

Full description:
https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/
"""
import re


def find_str(haystack: str, needle: str) -> int:
    index = -1

    for i in range(len(haystack)):
        if haystack[i] == needle[0] and haystack[i:len(needle)+i] == needle:
            return i

    return index


# Solution with regex
def str_str(haystack: str, needle: str) -> int:
    index = -1

    m = re.search(needle, haystack)
    if m:
        index = m.span()[0]

    return index
