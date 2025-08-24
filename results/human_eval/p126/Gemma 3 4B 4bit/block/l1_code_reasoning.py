def check_list(input_list):
    is_sorted = True
    for i in range(1, len(input_list)):
        if input_list[i] < input_list[i - 1]:
            is_sorted = False
            break
    seen_numbers = set()
    has_duplicates = False
    for num in input_list:
        if num in seen_numbers:
            has_duplicates = True
        else:
            seen_numbers.add(num)
    return is_sorted and (not has_duplicates)