"""
Given a string s containing just the characters '(', ')', '{', '}',
'[' and ']', determine if the input string is valid.

Full description:
https://leetcode.com/problems/valid-parentheses/
"""


def is_valid(s: str) -> bool:
    close_parentheses = {')': '(', ']': '[', '}': '{'}
    stack = list()

    stack.append(s[0])

    for p in s[1:]:
        if not stack and p in close_parentheses:
            return False
        elif p in close_parentheses and stack[-1] == close_parentheses[p]:
            stack.pop()
        else:
            stack.append(p)

    return not stack
