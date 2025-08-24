def sort_and_select(integer_list):
    sorted_list = sorted(integer_list)
    last_elements = sorted_list[-k:]
    return last_elements