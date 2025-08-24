def sum_of_distinct_triplets(dimensions, rule):
    vector = [rule(i) for i in range(dimensions)]
    total = 0
    for value in vector:
        if rule(value):
            total += value
    return total