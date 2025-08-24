def count_positive_digit_sums(int_list):
    count = 0
    for num in int_list:
        digit_sum = sum((int(d) for d in str(abs(num))))
        if digit_sum > 0:
            count += 1
    return count