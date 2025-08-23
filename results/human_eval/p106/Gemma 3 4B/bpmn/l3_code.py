def generate_list(n):
    """
    Generates a list of dimension n with values from 0 to n-1.

    Args:
        n: An integer representing the dimension of the list.

    Returns:
        A list of integers from 0 to n-1.
    """
    list_ = []
    i = 1
    while i <= n:
        x = 0
        j = 1
        while j <= i:
            x = j
            j += 1
        list_.append(x)
        i += 1
    return list_