def process_list(input_list):
    """
    Process a list of integers and return the sum of the first n elements.
    """
    n = len(input_list)
    sum = 0
    for i in range(n):
        sum += input_list[i]
    return sum