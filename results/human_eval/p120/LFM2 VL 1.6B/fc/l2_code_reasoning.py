def sort_list(int_list):
    if not int_list:
        return []
    if len(int_list) == 1:
        return int_list
    sorted_list = sorted(int_list)
    return sorted_list