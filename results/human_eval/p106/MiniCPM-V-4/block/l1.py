def f(n):
    """
    Returns a list of size n, where each element at index i is either the factorial of i if i is even,
    or the sum of numbers from 1 to i otherwise. The indices start from 1.
    """
    # Initialize an empty list to store the result
    result = []
    
    # Iterate over the range from 1 to n (inclusive)
    for i in range(1, n + 1):
        # Check if the current index i is even
        if i % 2 == 0:
            # If i is even, calculate the factorial of i using a loop or recursion
            factorial = 1
            for j in range(1, i + 1):
                factorial *= j
            # Append the calculated factorial to the result list
            result.append(factorial)
        else:
            # If i is odd, calculate the sum of numbers from 1 to i using the formula for sum of arithmetic series
            sum_of_numbers = i * (i + 1) // 2
            # Append the calculated sum to the result list
            result.append(sum_of_numbers)
    
    # Return the resulting list
    return result