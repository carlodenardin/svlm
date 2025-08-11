def maximum(arr, k):
    # Step 1: Sort the array in descending order to get the largest elements first.
    arr.sort(reverse=True)
    # Step 2: Return the first k elements of the sorted array as a list.
    return arr[:k]