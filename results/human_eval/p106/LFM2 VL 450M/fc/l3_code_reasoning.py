def is_equal(i: int, n: int) -> bool:
    step = 2
    while True:
        if step == 2:
            if i == n:
                return True
            step = 3
        elif step == 3:
            if i < n:
                step = 4
            else:
                if i == n:
                    return True
                step = 5
        elif step == 4:
            if i == n:
                return True
            else:
                step = 6
        elif step == 5:
            if i < n:
                step = 7
            else:
                if i == n:
                    return True
                step = 8
        elif step == 6:
            if i < n:
                step = 9
            else:
                if i == n:
                    return True
                step = 10
        elif step == 7:
            if i < n:
                step = 11
            else:
                if i == n:
                    return True
                step = 12
        elif step == 8:
            return False
        elif step == 9:
            if i < n:
                step = 11
            else:
                if i == n:
                    return True
                step = 10
        elif step == 10:
            if i < n:
                step = 11
            else:
                if i == n:
                    return True
                step = 8
        elif step == 11:
            if i < n:
                step = 12
            else:
                if i == n:
                    return True
                step = 12
        elif step == 12:
            return False
        else:
            return False