def first_recurring(array: list):
    # Check input
    if not all(isinstance(value, (int, float, tuple, str)) for value in array):
        raise TypeError('Invalid value in the array!')

    uniques = set()

    # Loop through array until the recurring will be found
    for character in array:
        if character in uniques:
            return character
        uniques.add(character)

    # If there are no matches
    return None


array_1 = [1, 2, (5, 6), [], 2, 7]  # => 2
array_2 = [5, 1, 1, 6, 9, 2]  # => 1
array_3 = [1, 2, 3, 4]  # => None
print(first_recurring(array_1))
print(first_recurring(array_2))
print(first_recurring(array_3))
