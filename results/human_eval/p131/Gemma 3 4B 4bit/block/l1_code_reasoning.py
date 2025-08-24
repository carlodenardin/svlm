def product_of_odd_digits(number: int) -> int:
    product = 1
    for ch in str(number):
        digit = int(ch)
        if digit % 2 != 0:
            product *= digit
    return product if product != 1 else 0