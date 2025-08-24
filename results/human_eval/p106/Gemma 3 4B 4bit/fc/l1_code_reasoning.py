def compute_sequence(n):
    """
    For i from 1 to n:
      - if i is even: compute product of 1..i
      - if i is odd: compute sum of 1..i
    Return the list of computed values.
    """
    result = []
    i = 1
    count = 0
    while i <= n:
        if i % 2 == 0:
            prod = 1
            j = 1
            while j <= i:
                prod *= j
                j += 1
            value = prod
        else:
            s = 0
            t = 1
            while t <= i:
                s += t
                t += 1
            value = s
        result.append(value)
        count += 1
        i += 1
    return result