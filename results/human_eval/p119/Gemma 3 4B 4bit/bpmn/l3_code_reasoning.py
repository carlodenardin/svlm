def check_contains_all_characters(s, str1):
    i = 0
    c = 0
    while i < len(s):
        j = 0
        while j < len(str1):
            if s[i] == str1[j]:
                c += 1
            j += 1
        if len(str1) < c:
            return False
        c -= 1
        i += 1
    return True