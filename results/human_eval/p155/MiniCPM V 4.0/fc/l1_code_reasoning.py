def count_even_odd_digits(n: int):
    even_count = 0
    odd_count = 0
    while n > 0:
        digit = n % 10
        if digit % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
        n //= 10
    return (even_count, odd_count)