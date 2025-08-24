def check_string(s):
    """
    Checks if a string composed of rounded parentheses is 'balanced'.
    Balanced means that every '(' has a matching ')' and
    the number never exceed openings in order.
    """
    s1 = 0
    s2 = 0
    for i in range(len(s)):
        if s[i] == '[':
            s1 += 1
        elif s[i] == ']':
            s2 += 1
        if s1 < s2:
            return False
    return s1 == s2