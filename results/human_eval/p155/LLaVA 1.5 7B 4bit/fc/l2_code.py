def extract_increase(remain, extract):
    if remain == 0:
        return 0
    else:
        return extract * (remain - 1) + extract