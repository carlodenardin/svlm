def is_prime_by_sequential_divisors(n: int) -> bool:
    """
    Check if n is prime by sequentially testing divisibility
    starting from 2 up to floor(sqrt(n)).
    Returns True if n is prime, False otherwise.
    This follows the described approach:
      1) Check divisibility by 2
      2) If not divisible, check by 3
      3) If not divisible, check by 4
      ...
      up to sqrt(n)
    """
    if n <= 1:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True