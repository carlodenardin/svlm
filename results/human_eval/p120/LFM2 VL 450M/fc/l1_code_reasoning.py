def sort_and_keep_last_k(input_list):
    """
    Implements the described algorithm:
    - Maintain an auxiliary list.
    - For each element, if it is less than the last element of the auxiliary list,
      append and sort in ascending order.
    - Otherwise, append and sort in descending order.
    Returns the final auxiliary list.
    """
    aux = []
    for x in input_list:
        if not aux:
            aux.append(x)
            aux.sort()
        elif x < aux[-1]:
            aux.append(x)
            aux.sort()
        else:
            aux.append(x)
            aux.sort(reverse=True)
    return aux