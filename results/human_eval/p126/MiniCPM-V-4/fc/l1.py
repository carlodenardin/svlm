def is_sorted(lst):
    if len(set(lst)) != len(lst):  # Check for duplicates
        return False
    for i in range(1, len(lst)):
        if lst[i] < lst[i-1]:  # Check if list is sorted
            return False
    return True