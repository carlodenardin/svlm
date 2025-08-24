def algorithm(n):
    """
    This function implements the algorithm described in the flowchart.

    Args:
        n: An integer.

    Returns:
        The product if n is odd, otherwise 0.
    """
    product = 1
    odd_flag = 0
    if n > 0:
        odd_flag = 0
        while n != 10:
            d = n % 10
            if d % 2 != 0:
                product = d
                odd_flag = 1
            else:
                n = n // 10
        if odd_flag == 1:
            return product
        else:
            return 0
    else:
        return 0