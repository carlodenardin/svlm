from itertools import combinations

def count_triples_multiple_of_3(n: int) -> int:
    a = [i * i - i + 1 for i in range(1, n + 1)]
    count = 0
    for triple in combinations(a, 3):
        if sum(triple) % 3 == 0:
            count += 1
    return count