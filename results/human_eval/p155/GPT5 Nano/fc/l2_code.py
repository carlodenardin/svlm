def count_even_odd_digits(num: int) -> tuple:
    even = 0
    odd = 0
    n = abs(num)
    while n > 0:
        digit = n % 10
        if digit % 2 == 0:
            even += 1
        else:
            odd += 1
        n //= 10
    return (even, odd)