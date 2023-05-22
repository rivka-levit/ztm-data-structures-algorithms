# O(n^2)
def max_sub_array(nums: list[int]) -> int:
    if not nums:
        return 0

    max_sum = nums[0]

    for i in range(len(nums)-1):
        current_sum = nums[i]
        j = i + 1

        while j < len(nums):
            current_sum += nums[j]
            if current_sum > max_sum:
                max_sum = current_sum
            j += 1

    return max_sum


# O(n)
def max_sub_array_2(nums: list[int]) -> int:
    if not nums:
        return 0

    max_sum = current_sum = nums[0]

    for n in nums[1:]:
        current_sum = max((current_sum + n), n)
        max_sum = max(max_sum, current_sum)

    return max_sum


input_1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]  # --> 6
input_2 = [1]  # --> 1
input_3 = [5, 4, -1, 7, 8]  # --> 23

print(max_sub_array_2(input_1))
print(max_sub_array_2(input_2))
print(max_sub_array_2(input_3))
