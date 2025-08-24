def odd_digit_product(n):
    n_str = str(n)
    product = 1
    if n % 2 != 0:
        for digit in n_str:
            d = int(digit)
            if d % 2 != 0:
                product *= d
        return product
    else:
        return 0