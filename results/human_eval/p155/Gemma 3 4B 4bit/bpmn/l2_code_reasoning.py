def count_even_odd_digits(n: int):
    """
    Returns a tuple (even_count, odd_count) for the digits of n.
    """
    s = str(abs(n))
    even = 0
    odd = 0
    for ch in s:
        d = int(ch)
        if d % 2 == 0:
            even += 1
        else:
            odd += 1
    return (even, odd)