def count_even_odd_digits(input_integer):
    even_count = 0
    odd_count = 0
    input_integer = abs(input_integer)
    string_integer = str(input_integer)
    for digit_char in string_integer:
        digit = int(digit_char)
        if digit % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return (even_count, odd_count)