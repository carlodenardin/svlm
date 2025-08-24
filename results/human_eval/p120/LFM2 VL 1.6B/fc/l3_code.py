def process_list(lst, k):
    sorted_lst = sorted(lst, key=lambda x: x[k])
    return sorted_lst[:k]