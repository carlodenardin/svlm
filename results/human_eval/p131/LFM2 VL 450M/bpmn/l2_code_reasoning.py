def solve():
    import sys
    s = sys.stdin.read().strip()
    if not s:
        return
    try:
        n = int(s)
    except ValueError:
        return
    if n % 2 != 0:
        print(0)
    elif n % 2 == 0:
        print(n)
    else:
        print(n)