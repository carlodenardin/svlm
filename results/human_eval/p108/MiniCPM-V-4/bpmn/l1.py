def count_nums(arr):
    count = 0
    for num in arr:
        if num > 0 or (num < 0 and sum(int(digit) for digit in str(abs(num))) > 0):
            count += 1
    return count