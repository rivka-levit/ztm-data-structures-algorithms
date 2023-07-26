"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways
can you climb to the top?

Full description:
https://leetcode.com/problems/climbing-stairs/
"""
from functools import lru_cache


# Solution with cache from functools
@lru_cache()
def ways_climb(n: int) -> int:
    if n == 1:
        return 1
    if n == 2:
        return 2
    return ways_climb(n-1) + ways_climb(n-2)


# Solution with cache inside the function
def ways_to_climb(n: int, cache=None) -> int:
    if n == 1:
        return 1
    if n == 2:
        return 2

    if cache is None:
        cache = dict()

    if n in cache:
        return cache[n]

    cache[n] = ways_to_climb(n - 1, cache) + ways_to_climb(n - 2, cache)
    return cache[n]


print(ways_to_climb(44))
