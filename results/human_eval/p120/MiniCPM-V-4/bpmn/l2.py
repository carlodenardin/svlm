def maximum(arr, k):
    if k > len(arr):
        return []
    
    # Sort the list in ascending order
    arr.sort()
    
    # Return the last k elements
    return arr[-k:]