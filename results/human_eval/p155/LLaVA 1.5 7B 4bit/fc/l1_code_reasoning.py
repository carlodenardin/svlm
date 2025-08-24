def count_even_odd_digits(n: int):
    """
    Count even and odd digits in the given integer n.
    Returns a tuple: (even_count, odd_count)
    """
    n = abs(n)
    even_count = 0
    odd_count = 0
    if n == 0:
        even_count += 1
        return (even_count, odd_count)
    while n > 0:
        digit = n % 10
        if digit % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
        n //= 10
    return (even_count, odd_count)