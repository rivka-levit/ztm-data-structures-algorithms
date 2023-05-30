def reverse_string_iterative_1(string: str) -> str:
    new_string = ''
    for ch in string[::-1]:
        new_string += ch
    return new_string


def reverse_string_iterative_2(string: str) -> str:
    return ''.join(list(string)[::-1])


def reverse_string_recursive(string: str) -> str:
    if len(string) <= 1:
        return string
    return string[-1] + reverse_string_recursive(string[:-1])


print(reverse_string_iterative_1('yoyo mastery'))
print(reverse_string_iterative_2('yoyo mastery'))
print(reverse_string_recursive('ab'))
