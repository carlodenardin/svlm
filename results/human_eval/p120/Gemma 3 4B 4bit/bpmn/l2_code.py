def get_last_k_elements(integer_list, k):
    """
  Receives a list of integers and a variable k.
  Sorts the list in ascending order.
  Returns the last k elements of the sorted list.
  """
    integer_list.sort()
    return integer_list[-k:]