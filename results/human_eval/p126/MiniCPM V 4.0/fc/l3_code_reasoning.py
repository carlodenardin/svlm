def find_duplicates_adjacent(l):
    """
    Print duplicates by comparing each element with its immediate predecessor.
    Follows the algorithm: start i at 1, loop while i < len(l), compare l[i] with l[i-1],
    and print when equal. Then (per the described steps) perform a final no-op check.
    """
    i = 1
    while i < len(l):
        if l[i] == l[i - 1]:
            print(l[i])
        i += 1
    if len(l) > 1:
        pass