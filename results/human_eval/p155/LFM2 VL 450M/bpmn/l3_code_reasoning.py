def determine_odd_as_per_algorithm(n: int) -> int:
    odd = 0
    even = 0
    for i in range(0, n):
        if i % 2 == 0:
            odd = 1
        else:
            even = 2
    return odd

def solve():
    import sys
    data = sys.stdin.read().strip().split()
    if not data:
        return
    n = int(data[0])
    result = determine_odd_as_per_algorithm(n)
    print(result)

if __name__ == "__main__":
    solve()