def generate_sequence(n, j=None):
    sequence = []
    x = 0
    while x < n:
        if x < n:
            sequence.append(x)
            x += 1
        else:
            continue
    sequence.append(x)
    return sequence