# My solution O(n^2)
def move_zeroes(nums: list[int]) -> list:
    for zero in range(len(nums)):
        if nums[zero] == 0:
            non_zero = zero
            while non_zero < len(nums) and nums[non_zero] == 0:
                non_zero += 1
            if non_zero != len(nums):
                nums[zero], nums[non_zero] = nums[non_zero], nums[zero]

    return nums


# Right solution O(n)
def move_zeroes_2(nums: list[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    # Initialize pointer to the beginning of the array
    i = 0
    # Loop through the array
    for j in range(len(nums)):
        # If the current element is non-zero
        if nums[j] != 0:
            # Swap it with the element at the current pointer
            nums[i], nums[j] = nums[j], nums[i]
            # Increment the pointer
            i += 1


numbers = [0, 1, 0, 3, 12]
move_zeroes_2(numbers)
print(numbers)
