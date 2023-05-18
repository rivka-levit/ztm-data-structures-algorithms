def merge_two_sorted_lists(arr1: list, arr2: list) -> list:
    # Check input
    if arr1 is None:
        return arr2
    if arr2 is None:
        return arr1

    merged_list = list()

    # Variables to iterate through the lists
    i = j = 0

    # Iterate and append the smallest value to results
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merged_list.append(arr1[i])
            i += 1
        else:
            merged_list.append(arr2[j])
            j += 1

    # If the first array is larger, append it to results
    if i < len(arr1):
        merged_list.extend(arr1[i:])

    # If the first array is larger, append it to results
    if j < len(arr2):
        merged_list.extend(arr2[i:])

    return merged_list


nums1 = [0, 2, 4, 5, 8, 13, 28]
nums2 = [1, 3, 4, 7, 20]
print(merge_two_sorted_lists(nums1, nums2))
