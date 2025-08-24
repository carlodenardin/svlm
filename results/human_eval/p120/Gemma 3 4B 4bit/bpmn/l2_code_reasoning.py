def get_last_k_elements(lst, k):
    if k <= 0:
        return []
    sorted_list = sorted(lst)
    if k >= len(sorted_list):
        return sorted_list[:]
    return sorted_list[-k:]