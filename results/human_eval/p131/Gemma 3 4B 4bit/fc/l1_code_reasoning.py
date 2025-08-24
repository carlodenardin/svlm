def factorial_positive(n):
    if not isinstance(n, int):
        raise TypeError('Input must be an integer.')
    if n <= 0:
        raise ValueError('Input must be a positive integer.')
    product = 1
    for i in range(1, n + 1):
        product *= i
    return product