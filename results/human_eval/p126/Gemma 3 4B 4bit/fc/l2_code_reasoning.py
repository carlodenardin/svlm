def contains_no_duplicates_vlm(nums: list[int]) -> bool:
    counts: dict[int, int] = {}
    n = len(nums)
    if n < 2:
        return True
    for i in range(n - 1):
        current = nums[i]
        nxt = nums[i + 1]
        if current > nxt:
            continue
        if current in counts:
            return False
        else:
            counts[current] = counts.get(current, 0) + 1
    for c in counts.values():
        if c > 1:
            return False
    return True