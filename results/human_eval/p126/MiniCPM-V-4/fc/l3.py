def is_sorted(lst):
    """
    Given a list of numbers, return whether or not they are sorted
    in ascending order. If list has more than 1 duplicate of the same
    number, return False. Assume no negative numbers and only integers.
    """
    # Initialize a variable to keep track of the previous element in the list
    # This will be used to compare with the current element later
    prev_element = None
    
    # Iterate over the list using the enumerate function, which returns both the index and value of each element
    for i, num in enumerate(lst):
        # Check if the current element is equal to the previous element
        # If it is, we have found a duplicate number in the list
        if prev_element is not None and num == prev_element:
            # If there is already another occurrence of the duplicate number before this one, return False
            if i > 1 and lst[i-1] == lst[i-2]:
                return False
            # Otherwise, break out of the loop as we don't need to check further elements
            break
        
        # Update the previous element for the next iteration
        prev_element = num
    
    # After iterating over the entire list, check if all elements are unique
    # If any two consecutive elements are equal, return False
    if i > 1 and lst[i-1] == lst[i-2]:
        return False
    
    # If we haven't returned False by now, the list must be sorted in ascending order
    return True