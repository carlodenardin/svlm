def top_k_desc_last(integer_list, k):
    sorted_list = sorted(integer_list, reverse=True)
    if k <= 0:
        return []
    if k >= len(sorted_list):
        return sorted_list
    return sorted_list[-k:]