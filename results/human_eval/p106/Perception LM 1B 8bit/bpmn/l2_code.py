def compute_factorial(n):
    i = 1
    while i <= n:
        if i % 2 == 0:
            i += 1
        else:
            return i
    return i

def factorial(n):
    return compute_factorial(n)