def factorials_up_to(n):
    if n < 1:
        return []
    result = []
    i = 1
    while i <= n:
        fact = 1
        j = 1
        while j <= i:
            fact *= j
            j += 1
        result.append(fact)
        i += 1
    return result