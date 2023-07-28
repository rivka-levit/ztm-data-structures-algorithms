"""
The count-and-say sequence is a sequence of digit strings defined
by the recursive formula:

countAndSay(1) = "1"
countAndSay(n) is the way you would "say" the digit string
from countAndSay(n-1), which is then converted into a different digit string.
To determine how you "say" a digit string, split it into the minimal
number of substrings such that each substring contains exactly one unique digit.
Then for each substring, say the number of digits, then say the digit.
Finally, concatenate every said digit.

Full description:
https://leetcode.com/problems/count-and-say/
"""


def count_and_say(n: int) -> str:
    if n == 1:
        return '1'

    prev_string = count_and_say(n-1)
    count = 0
    num = prev_string[0]
    current_string = ''

    for digit in prev_string:
        if digit == num:
            count += 1
        else:
            current_string += str(count) + num
            num = digit
            count = 1

    current_string += str(count) + num

    return current_string
