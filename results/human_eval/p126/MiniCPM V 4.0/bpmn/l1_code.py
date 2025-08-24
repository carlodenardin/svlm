def check_sorted_unique(integers):
    if sorted(set(integers)) == sorted(integers):
        return True
    else:
        return False