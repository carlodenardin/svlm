def solve(N):
    """Given a positive integer N, return the total sum of its digits in binary.

    Example
        For N = 1000, the sum of digits will be 1 the output should be "1".
        For N = 150, the sum of digits will be 6 the output should be "110".
        For N = 147, the sum of digits will be 12 the output should be "1100".

    Variables:
        @N integer
             Constraints: 0 ≤ N ≤ 10000.
    Output:
         a string of binary number
    """
    # Step 1: Convert the given input to an integer and store it in variable 'N'
    N = int(N)

    # Step 2: Initialize a variable 'sum_of_digits' to keep track of the sum of digits
    sum_of_digits = 0

    # Step 3: Iterate through each digit of the input number using while loop
    while N > 0:
        # Step 4: Extract the last digit of the number by taking modulo with 10
        digit = N % 10
        # Step 5: Add the extracted digit to the running sum
        sum_of_digits += digit
        # Step 6: Remove the last digit from the number by performing floor division with 10
        N //= 10

    # Step 7: Convert the final sum of digits into binary representation
    binary_representation = bin(sum_of_digits)[2:]

    # Step 8: Return the resulting binary number as a string
    return binary_representation