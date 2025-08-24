def add_two_numbers(a=None, b=None):
    """
    Implements the described flow:
    - Read first number
    - Read second number
    - Calculate the sum
    - Display the result
    - End
    If a or b are not provided, prompts the user for input.
    Returns the numeric sum.
    """
    if a is None:
        a = float(input('Enter first number: '))
    if b is None:
        b = float(input('Enter second number: '))
    result = a + b
    print(result)
    return result