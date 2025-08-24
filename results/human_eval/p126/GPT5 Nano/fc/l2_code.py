def check_list(lst: list[int]) -> bool:
    for i in range(len(lst) - 1):
        if lst[i] > lst[i + 1]:
            return False
    from collections import Counter
    counts = Counter(lst)
    if any((count > 2 for count in counts.values())):
        return False
    return True