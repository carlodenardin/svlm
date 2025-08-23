def check_even_odd(n):
    """
    This function checks if a number is even or odd and returns a tuple
    containing the number of even numbers and the number of odd numbers
    encountered up to that point.
    """
    even = 0
    odd = 0
    n = abs(n)
    while n != 0:
        if n > 0:
            d = n % 10
            if d == 0:
                even += 1
            else:
                odd += 1
        n = n // 10
    return (even, odd)