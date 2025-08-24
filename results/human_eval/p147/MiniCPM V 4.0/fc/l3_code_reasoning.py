def factorial_and_count(n):
    i = 1
    a = [0] * max(0, n)
    while i <= n:
        a[i - 1] = i * (i - 1) * i
        i += 1
    j = i
    count = 0
    k = 0
    while j < len(a):
        if k < len(a) and j + 2 < len(a):
            if (a[j] + a[j + 1] + a[j + 2]) % 3 == 0:
                count += 1
            j += 1
            k += 1
        else:
            j += 1
    fact = 1
    for t in range(1, max(0, n) + 1):
        fact *= t
    return (count, fact)