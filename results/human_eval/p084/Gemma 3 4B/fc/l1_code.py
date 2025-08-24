def sum_of_digits_to_binary_string(n: int) -> str:
    sum_of_digits = 0
    while n != 0:
        digit = n % 10
        sum_of_digits += digit
        n //= 10
    return bin(sum_of_digits)[2:]