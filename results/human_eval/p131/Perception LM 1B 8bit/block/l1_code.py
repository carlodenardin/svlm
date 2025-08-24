def compute_product(num):
    odd_digits = [int(digit) for digit in str(num) if digit % 2 != 0]
    product = 1
    for digit in odd_digits:
        product *= digit
    return product if product > 0 else 0