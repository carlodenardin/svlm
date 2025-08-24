def last_k_elements_sorted(numbers, k):
    sorted_nums = sorted(numbers)
    if k <= 0:
        return []
    return sorted_nums[-k:]