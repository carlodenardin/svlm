def sum_digits_to_binary(n):
    digit_sum = sum((int(d) for d in str(abs(n))))
    return bin(digit_sum)[2:]