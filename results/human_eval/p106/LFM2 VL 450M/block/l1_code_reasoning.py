def generate_list(n):
    for i in range(1, n + 1):
        lst = list(range(1, i + 1))
    return lst if n >= 1 else []