def even_odd_count(num):
    # Convert the integer into a string to easily iterate over each digit
    num_str = str(abs(num))  # Take the absolute value to handle negative numbers
    
    # Initialize counters for even and odd digits
    even_count = 0
    odd_count = 0
    
    # Iterate over each character (digit) in the string
    for digit in num_str:
        # Check if the digit is even or odd using the modulus operator
        if int(digit) % 2 == 0:
            # If the digit is even, increment the even counter
            even_count += 1
        else:
            # If the digit is odd, increment the odd counter
            odd_count += 1
    
    # Return a tuple with the counts of even and odd digits
    return (even_count, odd_count)