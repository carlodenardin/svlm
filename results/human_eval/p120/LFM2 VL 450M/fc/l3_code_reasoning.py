def sort_integers(arr):
    sorted_arr = []
    for x in arr:
        sorted_arr.append(x)
        i = len(sorted_arr) - 1
        while i > 0 and sorted_arr[i] < sorted_arr[i - 1]:
            sorted_arr[i], sorted_arr[i - 1] = (sorted_arr[i - 1], sorted_arr[i])
            i -= 1
    return sorted_arr