def even_odd_count(num):
    num = abs(num)  # Make sure the number is positive.
    even_count = odd_count = 0
    while num > 0:
        digit = num % 10  # Get the last digit of the number.
        if digit % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
        num //= 10  # Remove the last digit from the number.
    return (even_count, odd_count)