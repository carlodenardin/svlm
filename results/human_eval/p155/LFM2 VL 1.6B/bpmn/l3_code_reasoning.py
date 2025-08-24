import random

def compute_probability(n, p):
    p_current = float(p)
    successes = 0
    for i in range(1, int(n) + 1):
        r = random.random()
        if r < p_current:
            successes += 1
            p_current = p_current - successes / float(n)
        else:
            failures = i - successes
            p_current = p_current + failures / float(n)
    return p_current