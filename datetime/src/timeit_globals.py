from timeit import timeit


def factorial(n: int) -> int:
    if n == 0:
        return 1
    else:
        result = n * factorial(n-1)
        return result


duration_cache = timeit(
    stmt='factorial(500); factorial(400); factorial(450); factorial(350)',
    globals=globals(),
    number=10000,
)


print(f'factorial time: {round(duration_cache, 6)} seconds')
