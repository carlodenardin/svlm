def is_arithmetic_progression(list):
    i = 1
    while True:
        if i < len(list):
            if list[i] == list[i - 1] - 1:
                return False
            if i > 1 and list[i] - list[i - 1] == list[i - 1] - list[i - 2]:
                return False
            i += 1
        else:
            return True