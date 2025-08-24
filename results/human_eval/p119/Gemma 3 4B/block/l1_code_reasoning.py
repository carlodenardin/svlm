def is_combination_balanced(input_pair):
    string1 = input_pair[0]
    string2 = input_pair[1]
    combined_string = string1 + string2
    balance_count = 0
    for ch in combined_string:
        if ch == '(':
            balance_count += 1
        elif ch == ')':
            balance_count -= 1
            if balance_count < 0:
                return 'No'
    return 'Yes' if balance_count == 0 else 'No'