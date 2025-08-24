def solve():
    import sys
    data = sys.stdin.read().strip()
    if not data:
        return
    try:
        n = int(data)
    except ValueError:
        digits = [c for c in data if c.isdigit()]
        n = int(''.join(digits)) if digits else 0
    digits_sum = sum((int(ch) for ch in str(abs(n)) if ch.isdigit()))
    binary_str = bin(digits_sum)[2:]
    final_result = int(binary_str, 2) if binary_str else 0
    print(final_result)