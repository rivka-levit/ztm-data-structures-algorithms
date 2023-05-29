def factorial_recursive(number):
    if number < 0:
        raise ValueError('Only positive numbers or zero accepted!')
    if number <= 1:
        return 1
    return number * factorial_recursive(number-1)


def factorial_iterative(number):
    if number < 0:
        raise ValueError('Only positive numbers or zero accepted!')
    if number == 0:
        return 1
    product = 1
    for i in range(1, number+1):
        product *= i
    return product


print(factorial_recursive(8))
print(factorial_iterative(8))
