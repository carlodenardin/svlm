def solve(N):
    # Convert the integer to binary and remove the '0b' prefix
    binary_str = bin(N)[2:]
    
    # Initialize a variable to store the sum of digits in binary
    sum_of_digits = 0
    
    # Iterate over each character in the binary string
    for digit in binary_str:
        # Convert the character back to an integer and add it to the sum
        sum_of_digits += int(digit)
    
    # Return the sum as a string
    return str(sum_of_digits)