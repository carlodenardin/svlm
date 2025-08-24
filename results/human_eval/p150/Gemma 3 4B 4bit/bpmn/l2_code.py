def calculate(n, x, y):
    """
  Calculates a value based on the input integers n, x, and y.

  Args:
    n: An integer.
    x: An integer.
    y: An integer.

  Returns:
    The calculated value.
  """
    if n == 1:
        return y
    else:
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return y
        return x