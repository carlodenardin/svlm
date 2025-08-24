def count_even_odd(n):
    even_count = 0
    odd_count = 0
    for i in range(n):
        if i % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return (even_count, odd_count)