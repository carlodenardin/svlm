def count_zero_sum_subarrays(n):
    """
    Counts the number of subarrays in a vector of size n where the sum of the elements is equal to 0.

    Args:
        n: The size of the vector.

    Returns:
        The number of subarrays with a sum of 0.
    """
    A = [0] * n
    count = 0
    i = 0
    while i < len(A):
        j = i + 1
        k = j
        while k < len(A):
            sum_subarray = sum(A[i:k + 1])
            if sum_subarray == 0:
                count += 1
            k += 1
        i += 1
        j = i + 1
        while j < len(A):
            k = j
            while k < len(A):
                sum_subarray = sum(A[i:k + 1])
                if sum_subarray == 0:
                    count += 1
                k += 1
            j += 1
        i += 1
    return count