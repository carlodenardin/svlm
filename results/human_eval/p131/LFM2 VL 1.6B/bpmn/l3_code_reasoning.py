def vlm_search(arr, target):
    product = 1
    n = len(arr)
    if n % 2 == 1:
        return 0
    if n <= 0:
        return -1
    d = n % 10
    if d % 2 == 1:
        return d
    product = d
    if product % 2 == 0:
        return -1
    n //= 10
    if n % 2 == 1:
        return 0
    product = 1
    if product % 2 == 0:
        return -1
    return -1