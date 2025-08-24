def calculate_product(n):
    if n % 10 == 0:
        return 0
    else:
        d = n % 10
        if d % 2 == 0:
            return d * 10
        else:
            return n // 10