def count_even_odd_digits_from_input():
    even_count = 0
    odd_count = 0
    s = input('Enter an integer: ')
    for ch in s:
        digit = int(ch)
        if digit % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return (even_count, odd_count)