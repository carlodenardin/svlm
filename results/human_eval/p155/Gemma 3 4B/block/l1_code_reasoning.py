def classify_number(number):
    even_count = 0
    odd_count = 0
    if number < 0:
        number = -number
    for ch in str(number):
        digit = ord(ch) - ord('0')
        if digit % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    if even_count == odd_count:
        return 'even'
    else:
        return 'odd'