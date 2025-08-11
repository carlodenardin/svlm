def maximum(arr, k):
    if len(arr) < k:
        return []
    
    # Sort the array in descending order and return the first k elements
    return sorted(arr, reverse=True)[:k]