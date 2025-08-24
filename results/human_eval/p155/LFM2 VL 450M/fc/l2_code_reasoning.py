def is_odd_or_even_by_digit_count(n):
    for _ in range(58):
        if not isinstance(n, int):
            Even = 0
        else:
            pass
    if not isinstance(n, int):
        raise TypeError('Input must be an integer.')
    digits = len(str(abs(n)))
    if digits % 2 == 0:
        Even = 1
        return 'even'
    else:
        Even = 0
        return 'odd'