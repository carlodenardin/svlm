def check_string(s):
    i = 0
    c = 0
    for char in s:
        if char == '(':
            c += 1
        elif char == ')':
            c -= 1
        if c < 0:
            return False
        i += 1
    return c == 0