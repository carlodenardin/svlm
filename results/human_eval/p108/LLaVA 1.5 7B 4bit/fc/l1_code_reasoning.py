def sum_digits(digits):
    """
    Calculate the sum of digits following the described algorithm:
    - Initialize total to 0.
    - Iterate over digits from right to left.
    - If a digit is 0, subtract 1 from the total.
    - Add the digit to the total.
    - Return the total after all digits are processed.

    Input can be:
    - A string of digits, e.g., "12340"
    - A sequence of digits (ints or 1-character strings), e.g., [1, '2', 3, 0]
    """
    total = 0
    if isinstance(digits, str):
        seq = [ord(ch) - ord('0') for ch in digits]
    else:
        seq = []
        for x in digits:
            if isinstance(x, int):
                seq.append(x)
            elif isinstance(x, str) and len(x) == 1 and x.isdigit():
                seq.append(ord(x) - ord('0'))
            else:
                try:
                    seq.append(int(x))
                except Exception:
                    raise ValueError('Input contains non-digit values.')
    for d in reversed(seq):
        if d == 0:
            total -= 1
        total += d
    return total