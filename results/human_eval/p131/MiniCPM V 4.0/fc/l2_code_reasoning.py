def product_of_odd_digits(n: int):
    s = str(abs(n))
    has_odd = False
    for ch in s:
        if (ord(ch) - ord('0')) % 2 == 1:
            has_odd = True
            break
    if not has_odd:
        return None
    product = 1
    for ch in s:
        d = ord(ch) - ord('0')
        if d % 2 == 1:
            product *= d
    return product