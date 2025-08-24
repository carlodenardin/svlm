def convert_to_binary_of_sum_of_digits(n: int) -> str:
    if n < 0:
        raise ValueError('Input must be a non-negative integer.')
    digit_sum = sum((int(ch) for ch in str(n)))
    return bin(digit_sum)[2:]