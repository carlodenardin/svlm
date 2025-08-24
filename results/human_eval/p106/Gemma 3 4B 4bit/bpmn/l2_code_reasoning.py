def generate_sum_and_factorial_list(n):
    result_list = []
    i = 1
    while i <= n:
        sum_to_i = sum(range(1, i + 1))
        factorial_i = 1
        for j in range(1, i + 1):
            factorial_i *= j
        result_list.append(sum_to_i)
        result_list.append(factorial_i)
        i += 1
    return result_list