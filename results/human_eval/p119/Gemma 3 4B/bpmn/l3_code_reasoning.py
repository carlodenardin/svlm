def is_substring_of_concatenation(string1, string2, s):
    combined_string = string1 + string2
    i = 0
    c = 0
    if i != 0:
        while i != 0:
            i += 1
            c += 1
            if len(combined_string) < len(s):
                c = 0
            elif s in combined_string:
                return True
            break
    elif len(combined_string) >= len(s) and s in combined_string:
        return True
    return False