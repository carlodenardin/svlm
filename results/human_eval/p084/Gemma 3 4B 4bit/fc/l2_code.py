def binary_of_digit_sum(n: int) -> str:
    total = 0
    while n != 0:
        last_digit = n % 10
        total += last_digit
        n //= 10
    res = ''
    while total > 0:
        rem = total % 2
        res += str(rem)
        total //= 2
    return res