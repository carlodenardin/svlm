def sum_digits_to_binary(n: int) -> str:
    sum_of_digits = 0
    while n > 0:
        sum_of_digits += n % 10
        n //= 10
    return bin(sum_of_digits)