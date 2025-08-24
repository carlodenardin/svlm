def generate_list(n):
    """
    Generates a list of dimension n with values initialized to 1.
    The list is appended with values x and j, where x is initialized to 0 and j starts from 1.
    """
    result = [[1] * n for _ in range(n)]
    for i in range(n):
        x = 0
        j = 1
        while j <= n:
            result[i].append(x)
            x += 1
            j += 1
    return result