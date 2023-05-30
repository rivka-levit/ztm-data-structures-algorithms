def bubble_sort(array: list) -> None:
    for i in range(len(array)-1, -1, -1):
        for j in range(i):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]


numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
bubble_sort(numbers)
print(numbers)
