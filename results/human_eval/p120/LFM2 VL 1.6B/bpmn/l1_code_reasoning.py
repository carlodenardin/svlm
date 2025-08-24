def sort_last_k_elements(lst, k):
    sorted_list = []
    for i in range(len(lst)):
        if len(sorted_list) < k:
            sorted_list.append(lst[i])
        else:
            sorted_list.append(lst[i])
    return sorted_list