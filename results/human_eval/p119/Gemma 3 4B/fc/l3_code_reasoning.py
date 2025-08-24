def contains_non_lowercase_dash(s: str) -> bool:
    i = 0
    c = 0
    s_local = s
    if len(s_local) == 0:
        return False
    if c == 0:
        while c < len(s_local) and i < len(s_local):
            if s_local[i] == '-':
                c += 1
            i += 1
    return c > 0