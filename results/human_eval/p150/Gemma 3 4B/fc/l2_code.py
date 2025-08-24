def find_smallest_prime(n):
    """
    Finds the smallest prime factor of a given integer n.

    Args:
        n: An integer.

    Returns:
        The smallest prime factor of n.
        If n is 1, returns 'y'.
        If no prime factor is found, returns n.
    """
    if n == 1:
        return 'y'
    for x in range(2, int(n ** 0.5) + 1):
        if n % x == 0:
            is_prime = True
            for i in range(2, int(x ** 0.5) + 1):
                if x % i == 0:
                    is_prime = False
                    break
            if is_prime:
                return x
            else:
                continue
    return n