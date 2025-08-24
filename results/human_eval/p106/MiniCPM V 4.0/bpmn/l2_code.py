def compute_sum_and_factorial(n):
    result_list = []
    for i in range(1, n + 1):
        if i <= n:
            sum_value = sum(range(1, i + 1))
            result_list.append(sum_value)
        else:
            factorial_value = 1
            for j in range(1, i + 1):
                factorial_value *= j
            result_list.append(factorial_value)
        i += 1
    return result_list