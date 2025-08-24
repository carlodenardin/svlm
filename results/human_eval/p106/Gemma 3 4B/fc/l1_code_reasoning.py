def compute_values(n):
    """
    For i from 1 to n:
        if i is even: value = product of 1..i
        else: value = sum of 1..i
    Return the list of these values.
    """
    result = []
    i = 1
    counter = 0
    while i <= n:
        if i % 2 == 0:
            prod = 1
            for k in range(1, i + 1):
                prod *= k
            value = prod
        else:
            value = i * (i + 1) // 2
        result.append(value)
        counter += 1
        i += 1
    return result