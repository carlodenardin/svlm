def get_last_k_elements(lst, k):
    sorted_lst = sorted(lst)
    return sorted_lst[-k:]