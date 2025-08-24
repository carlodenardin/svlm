def compute_product_list(n):
    result = []
    counter = 0
    calculated_value = None
    if n < counter:
        calculated_value = 1
        for i in range(1, n + 1):
            calculated_value *= i
    else:
        calculated_value = 1
        for i in range(1, n + 1):
            calculated_value *= i
        result.append(calculated_value)
        counter += 1
    return result