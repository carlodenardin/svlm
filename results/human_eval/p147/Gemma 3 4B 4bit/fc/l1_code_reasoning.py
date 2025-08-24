def count_distinct_pairs(n, vector):
    seen_pairs = set()
    vec = [0] * n
    for i in range(n):
        x = vector[i]
        y = vector[i]
        vec[i] = abs(x) + y + i
    count = 0
    for i in range(n):
        x = vec[i]
        for j in range(i + 1, n):
            y = vec[j]
            pair = (x, y)
            if pair not in seen_pairs:
                seen_pairs.add(pair)
                count += 1
    return count