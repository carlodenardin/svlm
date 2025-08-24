import sys

def solve():
    data = sys.stdin.read()
    s = data.strip().split()[0] if data.strip() else ''
    count = 0
    for ch in s:
        if ch == '0':
            count += 1
        elif ch == '1':
            count -= 1
    if count == 0:
        try:
            val = int(s, 10) if s else 0
        except ValueError:
            val = 0
        print(val)
    else:
        print(s)