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


if __name__ == '__main__':
    print(add_80(5))
    print(add_80(6))
    print(add_80(5))
