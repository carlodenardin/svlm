def solve(N):
    sum = 0
    res = ""
    while N > 0:
        sum += N % 10
        N //= 10
        r = sum % 2
        sum //= 10
        res += str(r)
    return res