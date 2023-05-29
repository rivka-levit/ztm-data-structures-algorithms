from functools import lru_cache


def fibonacci_iterative(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    prev = 0
    fib = 1
    for _ in range(2, n+1):
        fib, prev = fib + prev, fib
    return fib


@lru_cache()
def fibonacci_recursive(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)


print(fibonacci_iterative(100))
print(fibonacci_recursive(100))
