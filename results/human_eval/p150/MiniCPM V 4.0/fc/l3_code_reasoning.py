import math

def vlm_gcd(n_input, x, y_input):
    n = 1
    i = 2
    y = y_input
    while n != 0:
        if i <= int(math.sqrt(n)):
            rem = n % i
            if rem == 0:
                y = i
                break
        else:
            n = 0
            break
        i += 1
    return y