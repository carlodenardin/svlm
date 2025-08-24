def generate_list(n):
    """
    Generate a list according to the described algorithm:
    For i from 1 to n (inclusive), append the sum of numbers from 1 to i.
    If i is even, also append the factorial of i.
    """
    result = []
    i = 1
    while True:
        if i <= n:
            total = i * (i + 1) // 2
            result.append(total)
        else:
            break
        if i % 2 == 0:
            fact = 1
            for k in range(2, i + 1):
                fact *= k
            result.append(fact)
        i += 1
    return result