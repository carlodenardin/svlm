def sum_by_algorithm(arr):
    sum = 0
    for a in arr:
        if a == 1:
            sum += 1
        if a == 0:
            sum = 0
    for a in arr:
        if a == 1:
            sum += a
        if a == 0:
            sum = sum + a
    return sum