def calculate_even_product_odd_sum(n):
    result = []
    i = 1
    while i <= n:
        if i % 2 == 0:
            product = 1
            for num in range(1, i + 1):
                product *= num
            result.append(product)
        else:
            total = sum(range(1, i + 1))
            result.append(total)
        i += 1
    return result