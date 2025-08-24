def dimensions_from_n(n: int):
    """
    Generate a list of dimensions from an input integer n, following the described steps.
    """
    if not isinstance(n, int) or n <= 0:
        return []
    dimensions = []
    i = 1
    while i <= n:
        faccofaces = [k for k in range(1, i + 1) if (k + i) % 2 == 0]
        if len(faccofaces) % 2 == 0:
            result = sum(faccofaces)
        else:
            result = sum(range(1, n + 1))
        dimensions.append(result)
        i += 1
    return dimensions