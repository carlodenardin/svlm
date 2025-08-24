def validate_list(nums):
    if nums != sorted(nums):
        return False
    from collections import Counter
    counts = Counter(nums)
    if any((count > 2 for count in counts.values())):
        return False
    return True