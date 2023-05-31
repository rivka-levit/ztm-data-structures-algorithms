def quick_sort(array: list) -> list:

    def swap(arr: list, index_1: int, index_2: int) -> None:
        arr[index_1], arr[index_2] = arr[index_2], arr[index_1]

    def get_pivot(arr: list, pivot_index: int, end_index: int) -> int:
        swap_index = pivot_index

        for i in range(pivot_index + 1, end_index + 1):
            if arr[i] < arr[pivot_index]:
                swap_index += 1
                swap(arr, swap_index, i)

        swap(arr, pivot_index, swap_index)
        return swap_index

    def helper(arr: list, left: int, right: int) -> list:
        if left < right:
            pivot_index = get_pivot(arr, left, right)
            helper(arr, left, pivot_index - 1)
            helper(arr, pivot_index + 1, right)
        return arr

    return helper(array, 0, len(array) - 1)


numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
print(quick_sort(numbers))
