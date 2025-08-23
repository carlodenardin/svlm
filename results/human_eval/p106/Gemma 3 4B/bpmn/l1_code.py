def generate_list(n):
    """
    Generates a list of dimension n by repeatedly computing the factorial if i is even,
    or the sum of values from 1 to i if i is odd, and appending the result to the list.

    Args:
        n: An integer representing the dimension of the list.

    Returns:
        A list of dimension n.
    """
    my_list = []
    for i in range(1, n + 1):
        if i % 2 == 0:
            factorial = 1
            for j in range(1, i + 1):
                factorial *= j
            my_list.append(factorial)
        else:
            sum_val = 0
            for j in range(1, i + 1):
                sum_val += j
            my_list.append(sum_val)
    return my_list