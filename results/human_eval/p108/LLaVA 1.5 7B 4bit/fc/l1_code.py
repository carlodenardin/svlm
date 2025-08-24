def count_digits(list_value):
    count = 0
    for i in list_value:
        if i.isdigit():
            count += 1
    return count