def count_even_odd_digits(n):
    n = abs(int(n))
    even_count = 0
    for ch in str(n):
        digit = int(ch)
        if digit % 2 == 0:
            even_count += 1
    odd_count = 0
    for ch in str(n):
        digit = int(ch)
        if digit % 2 != 0:
            odd_count += 1
    return (even_count, odd_count)