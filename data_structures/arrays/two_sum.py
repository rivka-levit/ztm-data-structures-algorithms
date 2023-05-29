def two_sum(nums: list[int], target: int) -> list:
    visited = dict()

    for i in range(len(nums)):
        compliment = target - nums[i]
        if compliment in visited:
            return [visited[compliment], i]
        visited[nums[i]] = i


print(two_sum([3, 3], 6))
