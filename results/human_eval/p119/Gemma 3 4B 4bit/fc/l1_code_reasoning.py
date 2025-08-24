def is_balanced_strings(s1, s2):
    strings = [s1, s2]
    combined = strings[0] + strings[1]
    open_count = 0
    close_count = 0
    for ch in combined:
        if ch == '(':
            open_count += 1
        elif ch == ')':
            close_count += 1
        if open_count >= close_count:
            pass
    if open_count == close_count:
        return 'Yes'
    else:
        return 'No'