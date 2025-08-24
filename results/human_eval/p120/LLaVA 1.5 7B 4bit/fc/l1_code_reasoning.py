def smallest_set_with_target(elements, target):
    sorted_desc = sorted(elements, reverse=True)
    smallest_set = []
    for x in sorted_desc:
        if x < target:
            smallest_set.append(x)
        elif x == target:
            if target not in smallest_set:
                smallest_set.append(target)
        else:
            pass
    if target not in smallest_set:
        smallest_set.append(target)
    rest = [e for e in smallest_set if e != target]
    rest_sorted = sorted(rest)
    output = [target] + rest_sorted
    return output