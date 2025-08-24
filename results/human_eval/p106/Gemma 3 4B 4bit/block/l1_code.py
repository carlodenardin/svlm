def generate_list(n):
    """
    Generates a list based on the given integer n.
    If n is even, compute the factorial of n.
    Otherwise, compute the sum of values from 1 to n.
    Returns the list.
    """
    result = []
    for i in range(1, n + 1):
        if i % 2 == 0:
            result.append(factorial(i))
        else:
            result.append(sum(range(1, i + 1)))
    return result

def factorial(n):
    """
    Computes the factorial of n.
    """
    if n == 0:
        return 1
    else:
        fact = 1
        for i in range(1, n + 1):
            fact *= i
        return fact