def sort_integers(input_list):
    if len(input_list) == 0:
        return True
    if len(input_list) == 1:
        return False
    if input_list[0] > input_list[1]:
        return sort_integers(input_list[1:])
    else:
        return sort_integers(input_list[1:])