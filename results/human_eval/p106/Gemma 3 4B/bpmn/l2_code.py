def generate_list(n):
    """
    Generates a list based on the given integer n.

    The list contains the sum from 1 to n and the factorial of n.
    """
    my_list = [1]
    i = 1
    while i <= n:
        if i % 2 == 0:
            my_list.append(sum(range(1, i + 1)))
        else:
            my_list.append(factorial(i))
        i += 1
    return my_list