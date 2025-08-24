def sum_of_digits(arr):
    res = 0
    while arr:
        res += arr[0]
        arr = arr[1:]
    return res

def main(arr):
    arr = [int(x) for x in arr]
    if sum_of_digits(arr) > 0:
        print("The sum of the digits is positive.")
    else:
        print("The sum of the digits is negative.")