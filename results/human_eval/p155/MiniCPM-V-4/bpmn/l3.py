def even_odd_count(num):
    """
    Given an integer. 
    Return a tuple that has the number of even and odd digits respectively.

    Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    # Convert the integer to its absolute value to handle negative numbers
    num = abs(num)
    
    # Initialize variables to keep track of even and odd counts
    even_count = 0
    odd_count = 0
    
    # Loop through each digit in the number
    while num > 0:
        # Get the last digit of the number
        digit = num % 10
        
        # Increment the count based on whether the digit is even or odd
        if digit % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
        
        # Remove the last digit from the number
        num //= 10
    
    # Return the counts as a tuple
    return even_count, odd_count