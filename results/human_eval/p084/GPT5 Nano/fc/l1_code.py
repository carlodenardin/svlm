def sum_digits_to_binary(n: int) -> str:
    digit_sum = sum((int(d) for d in str(abs(n))))
    binary_result = bin(digit_sum)[2:]
    return binary_result