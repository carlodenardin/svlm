def least_significant_set_of_digits(numbers):
    if not numbers:
        return 0
    if all((n == 1 for n in numbers)):
        return 1
    last_sum = None
    for n in numbers:
        s = sum((int(ch) for ch in str(abs(n))))
        last_sum = s
        if s == 0:
            return 1
    if last_sum == 0:
        return last_sum
    else:
        return last_sum