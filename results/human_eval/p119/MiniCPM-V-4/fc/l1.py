def match_parens(lst):
    # Check if both strings are empty, in which case we can concatenate them to form a good string
    if not lst or len(lst[0]) == 0 and len(lst[1]) == 0:
        return 'Yes'

    # If either string has more opening parentheses than closing parentheses, it cannot be made into a good string
    if len(lst[0]) > len(lst[1]):
        return 'No'
    if len(lst[0]) < len(lst[1]):
        return 'No'

    # Initialize counters for open and close parentheses
    open_count = 0
    close_count = 0

    # Concatenate the two strings
    concatenated_string = lst[0] + lst[1]

    # Iterate over the concatenated string
    for char in concatenated_string:
        # If the character is an opening parenthesis, increment the open count
        if char == '(':
            open_count += 1
        # If the character is a closing parenthesis, decrement the close count
        elif char == ')':
            close_count -= 1

    # If all parentheses are balanced, return 'Yes', otherwise return 'No'
    if open_count == close_count:
        return 'Yes'
    else:
        return 'No'