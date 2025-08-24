def count_positive_digit_sums(arr: list[int]) -> int:
    res = 0
    for num in arr:
        digits = [int(d) for d in str(abs(num))]
        s = sum(digits)
        if s > 0:
            res += 1
    return res