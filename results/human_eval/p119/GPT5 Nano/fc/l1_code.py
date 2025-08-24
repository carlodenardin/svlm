def is_balanced_parentheses_concatenation(strings):

    def is_balanced(s):
        count = 0
        for char in s:
            if char == '(':
                count += 1
            elif char == ')':
                count -= 1
                if count < 0:
                    return False
        return count == 0
    if len(strings) != 2:
        raise ValueError('Input must be a list of 2 strings.')
    concat1 = strings[0] + strings[1]
    concat2 = strings[1] + strings[0]
    if is_balanced(concat1) or is_balanced(concat2):
        return 'Yes'
    else:
        return 'No'