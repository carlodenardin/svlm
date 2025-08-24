def is_valid_index(lst, i):
    """
    Implements the described flowchart logic.
    Note: The input i is not used in the decision process according to the flowchart.
    Returns True if the index would be considered valid by that logic.
    """
    if len(lst) < 1:
        return True
    idx = 1
    while True:
        idx += 1
        if idx < len(lst):
            return True
        if idx > 1:
            return False