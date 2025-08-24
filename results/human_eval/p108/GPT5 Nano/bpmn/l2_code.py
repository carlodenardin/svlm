def count_positive_signed_digit_sums(int_list):
    res = 0
    for num in int_list:
        signed_digit_sum = sum((int(digit) if c != '-' else -int(digit) for c, digit in zip(str(num), str(num).lstrip('-'))))
        if signed_digit_sum > 0:
            res += 1
    return res