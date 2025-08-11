def solve(N):
    # Convert N to string and remove the decimal point
    N = str(N).replace('.', '')
    # Initialize sum of digits as 0
    sum_of_digits = 0
    # Iterate through each digit in N
    for digit in N:
        # Add the integer value of the current digit to sum_of_digits
        sum_of_digits += int(digit)
    # Convert sum_of_digits to binary using bin() function
    binary_sum = bin(sum_of_digits)[2:]
    # Return the result as a string
    return binary_sum