def count_geq_k(list_k_k_int, k):
    """
    Counts how many elements in the input list are >= k by:
    - creating a copy of the list
    - sorting the copy in ascending order
    - iterating and counting elements >= k
    """
    lst = list_k_k_int.copy()
    lst.sort()
    count = 0
    for x in lst:
        if x >= k:
            count += 1
    return count