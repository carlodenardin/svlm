import sys

def solve():
    data = list(map(int, sys.stdin.read().strip().split()))
    if not data:
        return
    n, x, y = (data[0], data[1], data[2])
    if n == 1:
        print(y)
        return
    limit = int(n ** 0.5)
    found = False
    i = 2
    while i <= limit:
        if n % i == 0:
            found = True
            break
        i += 1
    if found:
        print(y)
    else:
        print(x)