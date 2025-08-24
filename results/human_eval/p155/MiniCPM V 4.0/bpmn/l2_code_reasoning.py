def count_even_odd_digits(n: int):
    """
    Counts even and odd digits in an integer n.
    Follows the described algorithm:
    - Initialize counters even and odd to 0
    - Convert the absolute value of n to a string to access digits
    - For each digit character, convert to int and update counters
    - Return a tuple (even, odd)
    """
    even, odd = (0, 0)
    digits = str(abs(n))
    for ch in digits:
        d = ord(ch) - ord('0')
        if d % 2 == 0:
            even += 1
        else:
            odd += 1
    return (even, odd)