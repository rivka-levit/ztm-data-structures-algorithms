def selection_sort(array: list) -> None:
    for i in range(len(array)-1):
        for j in range(i+1, len(array)):
            if array[j] < array[i]:
                array[i], array[j] = array[j], array[i]


numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
selection_sort(numbers)
print(numbers)
