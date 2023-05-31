def insertion_sort(array: list) -> None:
    for i in range(1, len(array)):
        j = i - 1
        while array[i] < array[j]:
            array.insert(j, array.pop(i))
            i = j
            j -= 1


numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
insertion_sort(numbers)
print(numbers)
