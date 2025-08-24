def count_even_odd(n):
    count_even = 0
    count_odd = 0
    for digit in str(n):
        if int(digit) % 2 == 0:
            count_even += 1
        else:
            count_odd += 1
    return (count_even, count_odd)