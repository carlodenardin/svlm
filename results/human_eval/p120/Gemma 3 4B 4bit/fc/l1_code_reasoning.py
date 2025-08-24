def sort_names_with_addresses(pairs):
    """
    Sorts a list of (name, address) pairs alphabetically by name using insertion sort,
    while keeping each name associated with its corresponding address.
    Returns a new list of (name, address) tuples in sorted order.
    """
    sorted_pairs = list(pairs)
    for i in range(1, len(sorted_pairs)):
        current = sorted_pairs[i]
        j = i - 1
        while j >= 0 and sorted_pairs[j][0] > current[0]:
            sorted_pairs[j + 1] = sorted_pairs[j]
            j -= 1
        sorted_pairs[j + 1] = current
    return sorted_pairs