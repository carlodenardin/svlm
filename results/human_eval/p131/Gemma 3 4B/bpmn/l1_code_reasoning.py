def product_of_odd_digits(n: int) -> int:
    product = 1
    while n > 0:
        digit = n % 10
        if digit % 2 != 0:
            product *= digit
        n //= 10
    return 0 if product == 1 else product