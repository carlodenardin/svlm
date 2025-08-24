def vlm_digit_product_is_odd(n: int):
    product = 1
    odd_flag = 0
    while n > 0:
        d = n % 10
        product = product * d
        if d % 2 != 0:
            odd_flag = 1
        n = n // 10
    if odd_flag == 1:
        return product
    else:
        return None