def solve(N):
    sum = 0
    res = ""
    while N > 0:
        digit = N % 10
        sum += digit
        N //= 10
    while sum > 0:
        res = str(sum % 2) + res
        sum //= 2
    return res