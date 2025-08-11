def even_odd_count(num):
    even = 0
    odd = 0
    n = abs(num)
    while n > 0:
        d = n % 10
        if d % 2 == 0:
            even += 1
        else:
            odd += 1
        n //= 10
    return (even, odd)