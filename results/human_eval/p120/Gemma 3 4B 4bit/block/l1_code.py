def get_last_k_elements(numbers, k):
    """
  Receives a list of integers and an integer k as input.
  Sorts the list and returns the list with the last k elements.
  """
    sorted_numbers = sorted(numbers)
    last_k = sorted_numbers[-k:]
    return last_k