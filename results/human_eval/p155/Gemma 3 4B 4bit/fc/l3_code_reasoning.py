def vlm_perfect_check(num):
    """
    Implements the described flowchart algorithm:
    - initializes even and odd sums
    - iterates over digits of abs(num) from least significant to most
    - updates sums according to the given rules, including the special handling when a digit is 0
    - returns the final (even, odd) sums after processing all digits
    """
    even = 0
    odd = 0
    n = abs(int(num))
    while True:
        if n <= 0:
            break
        d = n % 10
        if d == 0:
            n = n // 10
            if n == 0:
                break
            elif even % 2 == 0:
                even += 1
            else:
                odd += 1
            continue
        elif d % 2 == 0:
            even += d
        else:
            odd += d
        odd += d
        n = n // 10
        if n == 0:
            break
        elif even % 2 == 0:
            even += 1
        else:
            odd += 1
    return (even, odd)