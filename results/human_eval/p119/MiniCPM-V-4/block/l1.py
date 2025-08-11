def match_parens(lst):
    open_count = 0
    close_count = 0
    for string in lst:
        for char in string:
            if char == '(':
                open_count += 1
            elif char == ')':
                close_count += 1
        if close_count > open_count:
            return 'No'
    return 'Yes' if open_count == close_count else 'No'