def solve(data):
    """
    Process a sequence of numbers following a simple decision/loop flow:
      - If the value is positive, output value * 2.
      - If the value is zero, stop processing.
      - If the value is negative, output value - 1.
    Returns a list of results corresponding to processed inputs until a zero is encountered
    (zero acts as a break condition).
    """
    result = []
    for x in data:
        if x > 0:
            result.append(x * 2)
        elif x == 0:
            break
        else:
            result.append(x - 1)
    return result

def read_numbers_from_stdin():
    import sys
    nums = []
    for line in sys.stdin:
        for token in line.strip().split():
            try:
                if '.' in token or 'e' in token.lower():
                    nums.append(float(token))
                else:
                    nums.append(int(token))
            except ValueError:
                # Ignore tokens that are not numeric
                pass
    return nums

if __name__ == "__main__":
    nums = read_numbers_from_stdin()
    output = solve(nums)
    # Print as space-separated values; ensure integers are printed without .0 when possible
    out_strings = []
    for v in output:
        if isinstance(v, float) and v.is_integer():
            out_strings.append(str(int(v)))
        else:
            out_strings.append(str(v))
    print(" ".join(out_strings))