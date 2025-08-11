def solve(N):
    sum = 0
    res = ""
    while N > 0:
        sum += N % 10
        N //= 10
    res = bin(sum)[2:]
    return res