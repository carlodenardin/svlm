def product_of_odd_digits(n):
    """
  Calculates the product of the odd digits in an integer.

  Args:
    n: An integer.

  Returns:
    The product of the odd digits in n. If n has no odd digits, returns 0.
  """
    n_str = str(n)
    odd_digits = []
    for digit in n_str:
        digit = int(digit)
        if digit % 2 != 0:
            odd_digits.append(digit)
    if not odd_digits:
        return 0
    else:
        product = 1
        for digit in odd_digits:
            product *= digit
        return product