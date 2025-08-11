def even_odd_count(num):
    count = {'even': 0, 'odd': 0}
    while num > 0:
        digit = num % 10
        if digit % 2 == 0:
            count['even'] += 1
        else:
            count['odd'] += 1
        num //= 10
    return tuple(count.values())