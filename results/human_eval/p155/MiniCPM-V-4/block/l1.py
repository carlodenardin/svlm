def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

    Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    # Convert the input to string so we can iterate over each digit
    num_str = str(abs(num))
    
    # Initialize counters for even and odd digits
    even_count = 0
    odd_count = 0
    
    # Iterate over each character in the string representation of the number
    for char in num_str:
        # Check if the character is even or odd by converting it to an integer and checking its remainder when divided by 2
        if int(char) % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    
    # Return a tuple with the counts of even and odd digits
    return (even_count, odd_count)