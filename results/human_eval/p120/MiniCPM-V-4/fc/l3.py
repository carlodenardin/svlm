def maximum(arr, k):
    if len(arr) < k:
        return []
    return sorted(arr, reverse=True)[:k]