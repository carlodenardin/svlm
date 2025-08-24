def compute_result(number: int) -> int:
    product = 1
    for ch in str(number):
        digit = int(ch)
        product *= digit
    if product > 9:
        return number
    else:
        return product