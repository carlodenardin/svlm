def match_parens(lst):
    """
    You are given a list of two strings, both strings consist of open
    parentheses '(' or close parentheses ')' only.
    Your job is to check if it is possible to concatenate the two strings in
    some order, that the resulting string will be good.
    A string S is considered to be good if and only if all parentheses in S
    are balanced. For example, the string '(())()' is good, while the string
    '())' is not.
    Return 'Yes' if there's a way to make a good string, and return 'No' otherwise.
    Examples:
    match_parens(['()(', ')']) == 'Yes'
    match_parens([')', ')']) == 'No'
    """
    # Check if the input list has exactly two elements
    if len(lst) != 2:
        return 'Invalid input'

    # Extract the first and second strings from the list
    str1, str2 = lst[0], lst[1]

    # Base case: If either string is empty, we can always form a valid string by combining them
    if not str1 or not str2:
        return 'Yes'

    # Recursive case: Try concatenating the two strings in different orders
    # and recursively check if the resulting string is good
    return match_parens([str1, str2]) or match_parens([str2, str1])

# Test cases
print(match_parens(['()(', ')']))  # Yes
print(match_parens([')', ')]'))  # No
print(match_parens(['((', ')']))  # Yes
print(match_parens([')', '()']))  # No