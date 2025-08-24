def sum_digits_to_binary(n: int) -> str:
    digits = str(n)
    total = 0
    for ch in digits:
        total += int(ch)
    return bin(total)[2:]