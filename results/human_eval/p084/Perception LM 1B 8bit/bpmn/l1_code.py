def convert_to_binary(n):
    total = 0
    m = abs(n)
    while m:
        total += m % 10
        m //= 10
    return bin(total)[2:]