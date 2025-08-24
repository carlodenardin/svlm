from collections import Counter

def contains_duplicates(nums):

    def condition(arr):
        if len(arr) < 2:
            return True
        is_sorted = all((arr[i] <= arr[i + 1] for i in range(len(arr) - 1)))
        counts = Counter(arr)
        no_more_than_one_duplicate = all((c <= 2 for c in counts.values()))
        return is_sorted and no_more_than_one_duplicate
    if condition(nums):
        counts = Counter(nums)
        return any((c > 1 for c in counts.values()))
    if condition(nums):
        counts = Counter(nums)
        return any((c > 1 for c in counts.values()))
    counts = Counter(nums)
    return any((c > 1 for c in counts.values()))