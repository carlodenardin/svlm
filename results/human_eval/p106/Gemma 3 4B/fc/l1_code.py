def calculate_result(n):
    """
    Calculates a result based on the input integer n.
    If n is even, it calculates the product of numbers from 1 to n.
    Otherwise, it calculates the sum of numbers from 1 to n.
    The result is stored in a list and returned.

    Args:
        n: An integer.

    Returns:
        A list containing the calculated result.
    """
    result_list = []
    counter = 0
    if n >= 0:
        if n % 2 == 0:
            product = 1
            for i in range(1, n + 1):
                product *= i
            result_list.append(product)
        else:
            sum_val = 0
            for i in range(1, n + 1):
                sum_val += i
            result_list.append(sum_val)
    return result_list