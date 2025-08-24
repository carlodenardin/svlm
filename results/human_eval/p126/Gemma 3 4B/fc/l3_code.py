def check_list(list_):
    """
    Checks if a list contains an element that satisfies the following conditions:
    - The element is less than the length of the list.
    - The element is greater than half the length of the list.
    - The element is greater than 1 and less than 2.
    """
    i = 0
    while i < len(list_):
        if i < len(list_) and list_[i] < len(list_) and (list_[i] > len(list_) / 2) and (list_[i] > 1) and (list_[i] < 2):
            return True
        i += 1
    return False