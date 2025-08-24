def count_even_odd_digits(n):
    """
  Counts the number of even and odd digits in an integer.

  Args:
    n: An integer.

  Returns:
    A tuple containing the count of even digits and the count of odd digits.
  """
    even_count = 0
    odd_count = 0
    n = abs(n)
    if n == 0:
        return (0, 0)
    while n > 0:
        digit = n % 10
        if digit % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
        n //= 10
    return (even_count, odd_count)