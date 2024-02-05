def is_subsequence(s: str, t: str) -> bool:
    i = j = 0

    while i < len(s) and j < len(t):
        if t[j] == s[i]:
            i += 1
        j += 1

    return i == len(s)


print(is_subsequence('abc', 'ahbgdc'))
print(is_subsequence('axc', 'ahbgdc'))
print(is_subsequence('', 'ahbgdc'))
print(is_subsequence('b', 'abc'))
