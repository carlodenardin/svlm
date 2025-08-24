def count_even_odd_digits(n: int) -> tuple:
    even = 0
    odd = 0
    for digit in str(abs(n)):
        if int(digit) % 2 == 0:
            even += 1
        else:
            odd += 1
    return (even, odd)