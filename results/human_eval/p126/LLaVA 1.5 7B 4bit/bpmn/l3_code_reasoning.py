import re

def flow_algorithm(user_input):
    """
    Implements a simple decision-flow based on the described flowchart reasoning:
    - If numeric: compute and return its square as the result.
    - If string: inspect for keywords and perform actions accordingly:
        * loop/repeat: perform a small loop (sequence) of length n (default 3 or first number found).
        * sum/add: compute the sum of numbers found in the string (if any).
        * greet/hello: return a greeting message.
        * exit/quit: indicate an exit command.
        * default: if numbers are present, return their sum.
        * otherwise: return an unrecognized input message.
    """

    def extract_numbers(s):
        return [int(n) for n in re.findall('-?\\d+', s)]
    if isinstance(user_input, (int, float)):
        val = user_input
        return {'type': 'numeric', 'input': val, 'result': val * val}
    if isinstance(user_input, str):
        s = user_input.strip()
        lower = s.lower()
        nums = extract_numbers(s)
        if 'loop' in lower or 'repeat' in lower:
            n = nums[0] if nums else 3
            sequence = [i + 1 for i in range(n)]
            return {'type': 'loop', 'n': n, 'sequence': sequence}
        if 'sum' in lower or 'add' in lower:
            total = sum(nums) if nums else 0
            return {'type': 'function', 'action': 'sum_numbers', 'numbers': nums, 'result': total}
        if 'greet' in lower or 'hello' in lower:
            return {'type': 'function', 'action': 'greet', 'message': 'Hello!'}
        if 'exit' in lower or 'quit' in lower:
            return {'type': 'command', 'action': 'exit', 'message': 'Exiting'}
        if nums:
            return {'type': 'function', 'action': 'sum_numbers', 'numbers': nums, 'result': sum(nums)}
        return {'type': 'text', 'message': 'Unrecognized input.'}
    return {'type': 'error', 'message': 'Unsupported input type.'}