def process_integer(n):
    if n == 0:
        return [1]
    else:
        return [n, process_integer(n - 1)]