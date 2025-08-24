def initialize_counter_to_target(target: int) -> int:
    """
    Implements the described algorithm:
    - Start counter at 0
    - While counter != target:
        - If counter is a multiple of 3, increment by 1
        - Otherwise, do nothing
    - Return the final counter
    Note: If target != 0 and cannot be reached with this rule, the loop will be infinite.
    """
    counter = 0
    while counter != target:
        if counter % 3 == 0:
            counter += 1
    return counter