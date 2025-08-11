def maximum(arr, k):
    # step 1: Sort the input list in descending order
    sorted_arr = sorted(arr, reverse=True)
    # step 2: Return the last k elements of the sorted list
    return sorted_arr[-k:]