from typing import Iterable, Any

def compute_total_from_inputs(inputs: Iterable[Any]) -> float:
    """
    Implements the described flowchart algorithm:
    - Initialize a running total to zero.
    - For each input value:
        - If the value (interpreted as a number) is less than 5, add it to the running total.
        - Otherwise (value >= 5), do not add; proceed to the next input.
    - The process ends when there are no more inputs.
    Returns the final running total.
    """
    total = 0.0
    for item in inputs:
        try:
            value = float(item)
        except (ValueError, TypeError):
            continue
        if value < 5:
            total += value
    return total