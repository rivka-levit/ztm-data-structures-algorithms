"""
Write a function to find the longest common prefix string
amongst an array of strings.

If there is no common prefix, return an empty string "".

Full description:
https://leetcode.com/problems/longest-common-prefix/
"""


def common_prefix(strs: list[str]) -> str:
    prefix = strs[0]

    for word in strs[1:]:
        i = 0

        while i < len(prefix) and i < len(word) and prefix[i] == word[i]:
            i += 1

        prefix = prefix[:i]

    return prefix
