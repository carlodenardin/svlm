def is_sorted(lst):
    '''
    Given a list of numbers, return whether or not they are sorted
    in ascending order. If list has more than 1 duplicate of the same
    number, return False. Assume no negative numbers and only integers.

    Examples
    is_sorted([5]) ➞ True
    is_sorted([1, 2, 3, 4, 5]) ➞ True
    is_sorted([1, 3, 2, 4, 5]) ➞ False
    is_sorted([1, 2, 3, 4, 5, 6]) ➞ True
    is_sorted([1, 2, 3, 4, 5, 6, 7]) ➞ True
    is_sorted([1, 3, 2, 4, 5, 6, 7]) ➞ False
    is_sorted([1, 2, 2, 3, 3, 4]) ➞ True
    is_sorted([1, 2, 2, 2, 3, 4]) ➞ False
    '''
    # Check if the input list is empty
    if not lst:
        return True  # An empty list is considered sorted

    # Iterate through the list starting from the second element
    for i in range(1, len(lst)):
        # Check if the current element is smaller than the previous one
        if lst[i] < lst[i - 1]:
            return False  # The list is not sorted

    # Check for duplicates
    seen = set()
    for num in lst:
        if num in seen:
            return False  # Found a duplicate number
        seen.add(num)

    return True  # The list is sorted with no duplicates