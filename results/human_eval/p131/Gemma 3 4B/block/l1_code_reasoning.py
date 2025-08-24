def product_of_odd_digits(number: int) -> int:
    product = 1
    n = number
    while n > 0:
        digit = n % 10
        if digit % 2 != 0:
            product *= digit
        n //= 10
    if product == 1:
        return 0
    return product