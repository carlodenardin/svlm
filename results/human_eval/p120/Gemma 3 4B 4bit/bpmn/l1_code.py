def get_sorted_last_k_elements(data, k):
    """
  Receives a list of integers and a variable k.
  Returns the sorted list with only the last k elements.
  """
    if not isinstance(data, list):
        raise TypeError('Input data must be a list.')
    if not all((isinstance(x, int) for x in data)):
        raise ValueError('All elements in the list must be integers.')
    if not isinstance(k, int):
        raise TypeError('k must be an integer.')
    if k < 0:
        raise ValueError('k must be non-negative.')
    if k > len(data):
        raise ValueError('k cannot be greater than the length of the list.')
    last_k_elements = data[-k:]
    last_k_elements.sort()
    return last_k_elements