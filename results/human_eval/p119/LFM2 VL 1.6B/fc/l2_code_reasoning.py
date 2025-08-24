def is_balanced_string(s: str) -> bool:
    """
    Implements the described (flawed) balancing algorithm:
    - Use a stack (list) to store opening parentheses encountered.
    - For '(': push to stack.
    - For ')':
        - If stack is empty -> False
        - If last element is '(', append '(' to stack (instead of popping)
          if it is the matching opening. If not, return False.
    - At the end, return True if the stack is non-empty, else False.
    """
    stack = []
    for ch in s:
        if ch == '(':
            stack.append(ch)
        elif ch == ')':
            if not stack:
                return False
            if stack[-1] == '(':
                stack.append('(')
            else:
                return False
    return len(stack) > 0