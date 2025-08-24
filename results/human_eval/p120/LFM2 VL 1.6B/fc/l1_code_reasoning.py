def sort_and_return_last_k(integers, k):
    if k <= 0 or k > len(integers):
        return []
    sorted_integers = sorted(integers)
    return sorted_integers[-k:]