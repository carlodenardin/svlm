def isSorted(lst):
    sorted = False
    for i in range(len(lst) - 1):
        if lst[i] < lst[i + 1]:
            sorted = True
            break
    return sorted