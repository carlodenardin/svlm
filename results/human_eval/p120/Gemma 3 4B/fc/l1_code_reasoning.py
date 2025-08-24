def filter_list(items, K):
    sorted_items = sorted(items)
    filtered_items = []
    for item in sorted_items:
        if item == K:
            filtered_items.append(item)
    return filtered_items