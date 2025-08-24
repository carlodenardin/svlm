def generate_pascals_triangle(n):
    a = [0] * n
    count = 0
    i = 1
    while i <= n:
        if i <= n:
            a[i - 1] = i * (i - 1)
        i += 1
    j = i + 1
    k = 1
    while j < len(a):
        if j < len(a):
            k += 1
        if k < len(a):
            if a[k - 1] + a[j - 1] + a[k - 3] == 0:
                count += 1
        j += 1
    return count