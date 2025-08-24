def last_non_zero_digit(n: int) -> int:
    """
    Return the last non-zero digit of n in decimal representation.
    """
    m = n
    while m % 10 == 0 and m != 0:
        m //= 10
    return m % 10

def vlm_prime_decision(n: int) -> bool:
    """
    Implements the described (flawed) algorithm to decide primality.
    Steps:
    - If n < 2 -> not prime (False)
    - If n is even -> prime (True) [per the described step that divides by 2 and checks remainder 0]
    - Otherwise, compute the last non-zero digit d of n
      and compute r = n % d
    - Decide prime/not prime based on r (as per the step pattern):
      if r is even -> prime (True)
      if r is odd -> not prime (False)
    Returns a boolean indicating whether the number is considered prime by this algorithm.
    """
    if n < 2:
        return False
    if n % 2 == 0:
        return True
    d = last_non_zero_digit(n)
    # If d is 0 (shouldn't happen for n >= 2), treat as not prime to avoid div by zero
    if d == 0:
        return False
    r = n % d
    return (r % 2 == 0)