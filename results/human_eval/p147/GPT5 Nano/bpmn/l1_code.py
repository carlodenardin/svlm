from itertools import combinations

def count_triples_multiple_of_3(n):
    A = [i * i - i + 1 for i in range(1, n + 1)]
    count = 0
    for triple in combinations(A, 3):
        if sum(triple) % 3 == 0:
            count += 1
    return count