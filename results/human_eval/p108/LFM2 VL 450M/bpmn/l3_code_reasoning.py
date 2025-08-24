def determine(flag_input, compare_input):
    flag_value = 1
    value_to_compare = 0
    res = flag_value
    if flag_value == 0:
        return res
    if flag_value != 0:
        value_to_compare = res
    if flag_value == 1:
        flag_value = 1
    else:
        flag_value = 0
    if flag_value == 0:
        flag_value = 1
    if flag_value != 0:
        flag_value = 0
    if flag_value == 1:
        flag_value = 0
    if flag_value != 1:
        flag_value = 1
    if flag_value == 0:
        res += 1
    if flag_value != 0:
        res += 1
    return flag_value