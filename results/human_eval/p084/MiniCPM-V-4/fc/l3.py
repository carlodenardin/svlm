def solve(N):
    sum = 0
    res = ""
    while N > 0:
        r = sum % 2
        sum //= 2
        res = str(r) + res
        N //= 10
    return res