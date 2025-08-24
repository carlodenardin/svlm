import sys

def parse_two_numbers_from_string(s: str):
    s = s.strip()
    if not s:
        raise ValueError("Empty input")
    # If input uses a comma to separate numbers
    if ',' in s:
        parts = [p.strip() for p in s.split(',') if p.strip() != '']
        if len(parts) >= 2:
            return int(parts[0]), int(parts[1])
    # Otherwise, try whitespace-separated values
    parts = s.split()
    if len(parts) >= 2:
        return int(parts[0]), int(parts[1])
    raise ValueError("Could not parse two numbers")

def solve():
    data = sys.stdin.read()
    try:
        a, b = parse_two_numbers_from_string(data)
    except Exception:
        cleaned = data.replace('\n', ' ').strip()
        a, b = parse_two_numbers_from_string(cleaned)
    total = a + b
    print(total)

if __name__ == "__main__":
    solve()