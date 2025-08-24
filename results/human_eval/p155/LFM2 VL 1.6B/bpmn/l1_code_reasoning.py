def count_even_odd_digits(n: int) -> tuple[int, int]:
    """
    Counts the number of even and odd digits in the integer n.
    The digits are considered from the decimal representation of |n|.
    Returns a tuple (even_count, odd_count).
    """
    s = str(abs(n))
    even = 0
    for ch in s:
        digit = ord(ch) - ord('0')
        if digit % 2 == 0:
            even += 1
    odd = 0
    for ch in s:
        digit = ord(ch) - ord('0')
        if digit % 2 != 0:
            odd += 1
    return (even, odd)