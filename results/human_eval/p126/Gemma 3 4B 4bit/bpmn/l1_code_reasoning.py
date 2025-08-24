def is_sorted_and_no_duplicates(nums):
    from collections import Counter
    if nums is None:
        return False
    counts = Counter(nums)
    for c in counts.values():
        if c > 2:
            return False
    for i in range(1, len(nums)):
        if nums[i] < nums[i - 1]:
            return False
    sorted_nums = sorted(nums)
    for i in range(1, len(sorted_nums)):
        if sorted_nums[i] == sorted_nums[i - 1]:
            return False
    return True