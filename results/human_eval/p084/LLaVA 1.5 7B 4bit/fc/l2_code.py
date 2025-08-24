def sum_of_digits_via_flowchart(n: int) -> int:
    """
    Implements the described flowchart algorithm:
    - Convert the input number to a string of digits.
    - Iterate from the rightmost digit towards the left.
    - For each step, if possible take a two-digit chunk (the current and previous digit)
      and add the sum of its two digits to the total.
    - If a single digit remains (at the leftmost end), add it directly to the total.
    - Return the total sum of digits of the original number.
    """
    s = str(abs(n))
    total = 0
    i = len(s) - 1
    while i >= 1:
        total += int(s[i - 1]) + int(s[i])
        i -= 2
    if i == 0:
        total += int(s[0])
    return total