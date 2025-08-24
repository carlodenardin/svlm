def count_one(n):
    count = 0
    i = 1
    while i <= n:
        if i % len(a) == 0:
            count += 1
        i += 1
    return count