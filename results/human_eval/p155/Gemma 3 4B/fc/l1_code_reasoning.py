def count_even_odd_digits(n: int):
    """
    Count even and odd digits in the integer n.
    Returns a tuple: (even_count, odd_count)
    """
    even_count = 0
    odd_count = 0
    for ch in str(n):
        if ch.isdigit():
            digit = int(ch)
            if digit % 2 == 0:
                even_count += 1
            else:
                odd_count += 1
    return (even_count, odd_count)