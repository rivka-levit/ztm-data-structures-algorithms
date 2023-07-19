"""
Given two strings s and t, return true if t is an anagram of s,
and false otherwise.

Full description:
https://leetcode.com/problems/valid-anagram/
"""


def is_anagram(s: str, t: str) -> bool:
    chars_hash = dict()

    for ch in s:
        chars_hash[ch] = chars_hash.get(ch, 0) + 1

    for ch in t:
        if ch not in chars_hash:
            return False
        if chars_hash[ch] == 1:
            del chars_hash[ch]
        else:
            chars_hash[ch] -= 1

    return True if not chars_hash else False
