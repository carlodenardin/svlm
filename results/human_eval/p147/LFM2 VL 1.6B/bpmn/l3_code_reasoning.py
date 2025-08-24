def algorithm(n):
    i = 1
    vec = [i for _ in range(n)]
    counter = 0
    max_iters = 10000
    it = 0
    while it < max_iters:
        it += 1
        if counter < len(vec):
            counter += 1
        else:
            vec = [i for _ in range(n)]
        if vec == [i + 1] * n:
            return counter
        vec = [x + 1 for x in vec]
    return counter