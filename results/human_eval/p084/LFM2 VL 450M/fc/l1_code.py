def sum_digits_to_binary_string(n: int) -> str:
    total = sum((int(ch) for ch in str(abs(n)) if ch.isdigit()))
    return bin(total)[2:]