def has_duplicates(list):
    """
  Checks if a list of integers contains any duplicate elements.

  Args:
    list: A list of integers.

  Returns:
    True if the list contains duplicate elements, False otherwise.
  """
    i = 0
    while i < len(list):
        if i < len(list) - 1:
            if list[i] == list[i + 1]:
                return False
        elif i > 1 and abs(list[i - 1]) == abs(list[i]):
            return False
        i += 1
    return True