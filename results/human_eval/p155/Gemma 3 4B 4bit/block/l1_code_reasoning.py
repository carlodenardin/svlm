def analyze_number(number: int) -> str:
    if number < 0:
        number = abs(number)
    even_count = 0
    odd_count = 0
    while number > 0:
        digit = number % 10
        if digit % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
        number //= 10
    if even_count == odd_count:
        return 'even'
    else:
        return 'odd'