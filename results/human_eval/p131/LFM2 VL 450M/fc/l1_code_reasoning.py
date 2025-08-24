def product_of_positive_integers(numbers):
    product = 1
    for n in numbers:
        if n > 0:
            product *= n
        else:
            return product
    return product