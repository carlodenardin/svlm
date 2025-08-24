def generate_sequence(n):
    result = [0] * n
    i = 1
    while i <= n:
        x = 0
        j = 1
        while j <= i:
            x += 1
            j += 1
        result.append(x)
        i += 1
    return result