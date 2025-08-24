def check_pair_balance(strings):
    """
    Accepts a list or tuple of two strings, concatenates them,
    and returns "Yes" if the total number of '(' equals the total number of ')',
    otherwise returns "No".
    The algorithm follows: concatenate, count openings and closings, compare counts.
    """
    if not isinstance(strings, (list, tuple)) or len(strings) != 2:
        raise ValueError('Input must be a list or tuple of exactly two strings.')
    combined = strings[0] + strings[1]
    openings = combined.count('(')
    closings = combined.count(')')
    if openings == closings:
        return 'Yes'
    else:
        return 'No'