def check_string(s: str) -> bool:
    """
    Placeholder validity function.
    Returns True if the input string is non-empty after stripping whitespace.
    """
    return len(s.strip()) > 0

def run_string_validation_flow():
    """
    Implements the described flowchart:
    - Prompt the user for strings.
    - Use check_string to determine validity.
    - If valid, store in valid_strings.
    - If not valid, store in invalid_strings and prompt again.
    - End when the user types 'exit'.
    - Output the list of valid strings.
    """
    valid_strings = []
    invalid_strings = []

    while True:
        user_input = input("Enter a string (type 'exit' to finish): ")
        if user_input.strip().lower() == 'exit':
            break

        if check_string(user_input):
            # Valid: proceed to next node (collect as valid)
            valid_strings.append(user_input)
        else:
            # Not valid: save the string and return to input node
            invalid_strings.append(user_input)
            continue  # explicitly go back to input

    print("Valid strings:", valid_strings)
    return valid_strings

if __name__ == "__main__":
    run_string_validation_flow()