def analyze_even_odd_digits(n: int):
    s = str(n)
    even = 0
    odd = 0
    for ch in s:
        if ch.isdigit():
            d = ord(ch) - ord('0')
            if d % 2 == 0:
                even += 1
            else:
                odd += 1
    if even > odd:
        return 'more_even'
    elif odd > even:
        return 'more_odd'
    else:
        return 'equal'