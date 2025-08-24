def solve_last_k_sorted(nums, K):
    """
    Implements the described algorithm:
    - Initialize last_K to 0.
    - Iterate through nums:
        - If current value > last_K, set last_K to current value.
        - Else (current value <= last_K), return the last K elements of the sorted nums.
    - If the loop completes without triggering the else, return the last K elements of the sorted nums.
    """
    if K <= 0:
        return []
    last_K = 0
    for val in nums:
        if val > last_K:
            last_K = val
        else:
            return sorted(nums)[-K:]
    return sorted(nums)[-K:]