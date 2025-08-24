def check_list(lst):
    is_sorted = all((lst[i] <= lst[i + 1] for i in range(len(lst) - 1)))
    from collections import Counter
    counts = Counter(lst)
    no_more_than_one_duplicate = all((count <= 2 for count in counts.values()))
    return is_sorted and no_more_than_one_duplicate