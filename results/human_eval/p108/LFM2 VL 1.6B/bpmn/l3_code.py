def process_imagery(imagery_list):
    res = 0
    for i in imagery_list:
        if i < 0:
            return res
        elif i > 0:
            n = i
            if n == 0:
                continue
            else:
                n = abs(n)
                if n > 0:
                    res += n
                else:
                    res -= n
    return res