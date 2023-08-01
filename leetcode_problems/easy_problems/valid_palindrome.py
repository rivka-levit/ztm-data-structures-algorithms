"""
A phrase is a palindrome if, after converting all uppercase letters
into lowercase letters and removing all non-alphanumeric characters,
it reads the same forward and backward. Alphanumeric characters include
letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

Full description:
https://leetcode.com/problems/valid-palindrome/
"""


def is_palindrome_1(s: str) -> bool:
    start, end = find_next_chars(s, 0, (len(s) - 1))

    while start < end and start != end:
        if s[start].lower() != s[end].lower():
            return False
        start, end = find_next_chars(s, start+1, end-1)

    return True


def find_next_chars(string: str, start: int, end: int) -> tuple[int, int]:
    if not string[start].isalnum():
        while start < len(string) and not string[start].isalnum():
            start += 1
    if not string[end].isalnum():
        while end > 0 and not string[end].isalnum():
            end -= 1

    return start, end
