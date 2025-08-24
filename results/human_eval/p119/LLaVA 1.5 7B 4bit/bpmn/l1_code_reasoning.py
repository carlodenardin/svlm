def concatenate_two_strings(a: str, b: str):
    """
    Implements the described flowchart:
    - Initialize two empty strings
    - Append the first input to the first empty string
    - Append the second input to the second empty string
    - Return both resulting strings
    """
    s1 = ''
    s2 = ''
    s1 = s1 + a
    s2 = s2 + b
    return (s1, s2)