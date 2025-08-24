def vlm_check(I):
    from collections import Counter
    for i in range(len(I) - 1):
        if I[i] <= I[i + 1]:
            counts = Counter(I)
            if any((cnt > 2 for cnt in counts.values())):
                return 'False'
        else:
            return 'No'
    return 'End'