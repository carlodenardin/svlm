def can_concatenate_strings_to_balanced(strings):
    """
    Given a list of strings, determine if there exists a non-empty subset of strings
    such that in the subset, every distinct string occurs the same number of times.
    Returns "Yes" if such a subset exists, otherwise "No".
    """
    if not strings:
        return 'No'
    n = len(strings)
    for mask in range(1, 1 << n):
        subset = []
        for i in range(n):
            if mask >> i & 1:
                subset.append(strings[i])
        from collections import Counter
        counts = Counter(subset)
        if len(set(counts.values())) == 1:
            return 'Yes'
    return 'No'