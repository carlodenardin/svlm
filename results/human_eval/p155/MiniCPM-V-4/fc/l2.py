def even_odd_count(num):
    """
    Given an integer, return a tuple that has the number of even and odd digits respectively.

    Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    # Convert the absolute value of num to string to easily access each digit
    num_str = str(abs(num))
    
    # Initialize counters for even and odd digits
    even_count = 0
    odd_count = 0
    
    # Iterate over each character in the string representation of num
    for char in num_str:
        # Convert the character back to an integer to perform arithmetic operations
        digit = int(char)
        
        # Check if the digit is even or odd and increment the corresponding counter
        if digit % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    
    # Return a tuple containing the counts of even and odd digits
    return (even_count, odd_count)