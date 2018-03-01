def fibonacci(n):
    """Return the nth value in the fibonacci series."""
    x = 0
    y = 1
    return sum_series(n, x, y)


def lucas(n):
    """Return the nth value in the lucas numbers series."""
    x = 2
    y = 1
    return sum_series(n, x, y)


def sum_series(n, x=0, y=1):
    """Return the nth value in a given numbers series. Defaults to fibonacci series."""
    series = [x, y]
    for i in range(n):
        new = series[-2] + series[-1]
        series.append(new)
    return series[n - 1]


assert fibonacci(8) == 13  # tests fibonacci() and sum_series(), throws error if not functioning properly
assert lucas(8) == 29  # tests lucas() and sum_series(), throws error if not functioning properly
