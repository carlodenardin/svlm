def sum_two_numbers(a=None, b=None):
    if a is None:
        a = float(input())
    if b is None:
        b = float(input())
    total = a + b
    print(total)
    return total