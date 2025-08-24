def check_balanced_combinations(strings):

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
    a, b = strings
    combo1 = a + b
    combo2 = b + a
    if is_balanced(combo1) or is_balanced(combo2):
        return 'Yes'
    else:
        return 'No'