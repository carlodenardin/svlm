def count_zero_sum_subarrays(A):
    """
    Counts the number of subarrays in a given array A that have a sum of 0.

    Args:
        A: A list of integers.

    Returns:
        The number of subarrays with a sum of 0.
    """
    n = len(A)
    count = 0
    for i in range(n):
        if len(A) > 0:
            for j in range(i, n):
                current_sum = 0
                for k in range(i, j + 1):
                    current_sum += A[k]
                if current_sum == 0:
                    count += 1
    return count