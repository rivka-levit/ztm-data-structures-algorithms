"""
Given a sorted array of distinct integers and a target value, return the index
if the target is found. If not, return the index where it would be if it were
inserted in order.

You must write an algorithm with O(log n) runtime complexity.

Full description: https://leetcode.com/problems/search-insert-position/
"""


def search_insert(nums: list, target: int) -> int:
    start = 0
    end = len(nums) - 1

    if nums[-1] == target:
        return end
    if nums[-1] < target:
        return end + 1
    if nums[0] >= target:
        return 0

    while start < end:
        mid = (start + end) // 2
        if nums[mid] == target:
            return mid

        if nums[mid] < target:
            if end - mid == 1 and nums[end] > target:
                return end
            start = mid
        elif nums[mid] > target:
            if mid - start == 1 and nums[start] < target:
                return mid
            end = mid

    return start


print(search_insert([1, 3, 5, 6, 8, 9, 10], 19))
