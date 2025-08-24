def flowchart_algorithm(n: int) -> int:
    if n == 0:
        binary_str = '0'
    else:
        bits = []
        m = n
        while m > 0:
            bits.append(m % 2)
            m //= 2
        binary_str = ''.join((str(b) for b in reversed(bits)))
    sum_digits = 0
    for ch in binary_str:
        sum_digits += int(ch)
    decimal_result = 0
    for ch in str(sum_digits):
        decimal_result = decimal_result * 10 + int(ch)
    return decimal_result