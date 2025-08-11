def match_parens(lst):
    # Create a set to store the opening parentheses from one string and their corresponding closing parentheses from the other string.
    parentheses = set()
    # Create an empty list to store the concatenated strings in order of matching.
    result = []
    # Iterate through each pair of strings in the input list.
    for s1, s2 in lst:
        # For each string, iterate through its characters.
        for char in s1 + s2:
            # If the character is an opening parenthesis, add it to the set if it's not already present.
            if char == '(':
                if char not in parentheses:
                    parentheses.add(char)
            # If the character is a closing parenthesis, check if there's a matching opening parenthesis in the set.
            elif char == ')':
                if parentheses:
                    parentheses.remove(parentheses.pop())
                else:
                    return 'No'
    # Check if all opening parentheses have been matched with closing parentheses.
    if len(parentheses) == 0:
        return 'Yes'
    else:
        return 'No'