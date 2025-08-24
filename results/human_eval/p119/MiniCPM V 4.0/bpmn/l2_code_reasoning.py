import sys

def check_string(s: str) -> bool:
    balance = 0
    for ch in s:
        if ch == '(':
            balance += 1
        elif ch == ')':
            balance -= 1
            if balance < 0:
                return False
    return balance == 0

def solve():
    data = sys.stdin.read().split()
    if len(data) < 3:
        return  # Not enough input to proceed as per described algorithm

    s1, s2, s3 = data[0], data[1], data[2]

    # Concatenate in both possible orders and initialize c1, c2
    c1 = check_string(s1 + s2)
    c2 = check_string(s2 + s1)

    # Check the final provided string's balance
    if check_string(s3):
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    solve()