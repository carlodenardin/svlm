def generate_special_list(n):
    result = []
    for i in range(1, n + 1):
        if i % 2 == 0:
            factorial = 1
            for j in range(1, i + 1):
                factorial *= j
            result.append(factorial)
        else:
            sum_val = i * (i + 1) // 2
            result.append(sum_val)
    return result