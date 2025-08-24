def compute_product(input_sequence):
    if not isinstance(input_sequence, list) or not all((isinstance(x, int) for x in input_sequence)):
        return 'Error: Input must be a list of integers.'
    product = 1
    for digit in input_sequence:
        if digit % 2 != 0:
            product *= digit
    if product == 1:
        return 0
    else:
        return product