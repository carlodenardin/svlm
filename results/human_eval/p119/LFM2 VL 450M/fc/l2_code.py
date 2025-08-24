def check_string(s):
    if s.startswith('st'):
        return True
    elif s.startswith('str'):
        return s.startswith('check,') or s.startswith('string')
    else:
        return False