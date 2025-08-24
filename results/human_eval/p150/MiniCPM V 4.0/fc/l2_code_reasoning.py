def vlm_find_divisor(n_input, x_input, y_input):
    n = 1
    y = None
    while n == 1:
        divisor_found = False
        max_x = int(n ** 0.5)
        for x in range(2, max_x + 1):
            if n % x == 0:
                y = x
                divisor_found = True
        if divisor_found:
            continue
        else:
            break
    return y