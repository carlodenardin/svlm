def calculate_product(n):
    if n == 1:
        return 1
    else:
        return n * calculate_product(n - 1)