def maximum(arr, k):
    # step 1: check if k is greater than the length of the array
    if k > len(arr):
        # step 2: sort the array in ascending order
        arr.sort()
        # step 3: return the entire sorted array
        return arr
    else:
        # step 2: sort the array in ascending order
        arr.sort()
        # step 3: return the last k elements of the sorted array
        return arr[-k:]