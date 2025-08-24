def separate_even_odd_digits(n: int) -> tuple[int, int]:
    """
    Implements the described algorithm:
    - Initialize even and odd to 0
    - If n > 0, process digits from least significant to most significant
      by checking the last digit d = n % 10
      - if d is even, increment even
      - else, increment odd
      - remove last digit via n //= 10
    - If n <= 0, return (0, 0)
    - After processing, return (even, odd)
    """
    even = 0
    odd = 0
    if n > 0:
        while n > 0:
            d = n % 10
            if d % 2 == 0:
                even += 1
            else:
                odd += 1
            n //= 10
        return (even, odd)
    else:
        return (0, 0)