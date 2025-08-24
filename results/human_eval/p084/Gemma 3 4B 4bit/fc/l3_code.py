def algorithm(n):
    if not isinstance(n, int) or n <= 0:
        return ''
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    if total > 0:
        res = ''
        while total > 0:
            r = total % 2
            total //= 2
            res = str(r) + res
        return res
    else:
        return str(total)