def product_of_odd_digits(n: int) -> int:
    value = n
    product = 0
    while value != 0:
        digit = abs(value) % 10
        if digit % 2 != 0:
            product *= digit
        value //= 10
    if product == 0:
        return 0
    else:
        return product