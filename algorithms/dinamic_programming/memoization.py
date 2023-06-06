def memoized(func):
    cache = dict()

    def wrapper(n):
        if n not in cache:
            cache[n] = func(n)
        return cache[n]

    return wrapper


@memoized
def add_80(number):
    print('long time')
    return number + 80


@memoized
def fib(number):
    if number == 0:
        return 0
    if number == 1:
        return 1
    return fib(number-1) + fib(number-2)


if __name__ == '__main__':
    print(add_80(5))
    print(add_80(6))
    print(add_80(5))
    print(fib(9))
