def check_numbers(list_int):
    for i in range(len(list_int) - 1):
        if list_int[i] >= list_int[i + 1]:
            return False
    return True