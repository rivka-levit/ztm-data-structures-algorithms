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


# Bonus task
def first_recurring2(array: list):
    for i in range(len(array)-1):
        item_1 = array[i]
        for j in range(i+1, len(array)):
            item_2 = array[j]
            if item_2 == item_1:
                inner = first_recurring2(array[i+1:j])
                return inner if inner else item_2
    return None


array_1 = [1, 2, 6, 5, 2, 7]  # => 2
array_2 = [5, 1, 1, 5, 9, 2]  # => 1
array_3 = [1, 2, 3, 4]  # => None
print(first_recurring(array_1))
print(first_recurring2(array_1))
print(first_recurring(array_2))
print(first_recurring2(array_2))
print(first_recurring(array_3))
print(first_recurring2(array_3))
