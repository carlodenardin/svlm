def calculate(x, y, n):
    if n == 1:
        return x
    elif n <= sqrt(n):
        return x
    else:
        return calculate(n - 1, y, n)