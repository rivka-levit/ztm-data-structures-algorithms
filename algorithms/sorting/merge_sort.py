def merge(arr_1: list, arr_2: list) -> list:
    sorted_array = list()
    i = j = 0

    while i < len(arr_1) and j < len(arr_2):
        if arr_1[i] < arr_2[j]:
            sorted_array.append(arr_1[i])
            i += 1
        else:
            sorted_array.append(arr_2[j])
            j += 1

    if i < len(arr_1):
        sorted_array.extend(arr_1[i:])
    if j < len(arr_2):
        sorted_array.extend(arr_2[j:])

    return sorted_array


def merge_sort(arr: list):
    if len(arr) <= 1:
        return arr

    middle_index = len(arr) // 2

    left = arr[:middle_index]
    right = arr[middle_index:]

    return merge(merge_sort(left), merge_sort(right))


numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
answer = merge_sort(numbers)
print(answer)
