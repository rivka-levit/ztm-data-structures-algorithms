"""
Given two strings needle and haystack, return the index of the first
occurrence of needle in haystack, or -1 if needle is not part of haystack.

Full description:
https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/
"""


def find_first_occurrence_ind(haystack: str, needle: str) -> int:
    return haystack.find(needle)


if __name__ == '__main__':
    print(find_first_occurrence_ind('sadbutsad', 'sad'))
