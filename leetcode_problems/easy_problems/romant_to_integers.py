"""
Given a roman numeral, convert it to an integer.

Full description:
https://leetcode.com/problems/roman-to-integer/
"""


def roman_to_integers(s: str) -> int:
    symbols = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    result = prev = 0

    for ch in s[::-1]:
        if symbols[ch] >= prev:
            result += symbols[ch]
        else:
            result -= symbols[ch]
        prev = symbols[ch]

    return result


if __name__ == '__main__':
    print(roman_to_integers('MCMXCIV'))
