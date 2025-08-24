def check_list():
    start = True
    while start:
        l = list(int)
        for i in l:
            if i < l[i] or i == l[i]:
                start = False
        if start:
            print('Check if there are numbers that appear more than twice.')
        else:
            print('End')
        start = True