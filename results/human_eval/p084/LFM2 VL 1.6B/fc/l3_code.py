def vlm_algorithm(n_input, r):
    n = int(n_input)
    total_sum = 0.0
    result_str = ''
    max_iterations = 1000
    iterations = 0
    while n > 0 and iterations < max_iterations:
        n = n * 10
        if n > 0:
            result_str += str(n)
        else:
            result_str += str(n)
        total_sum += 0.1
        n = n + 0.1
        iterations += 1
    return result_str