def calculate_sum_of_distinct_triples(A):
    n = len(A)
    A = [i * i - i + 1 for i in range(1, n)]
    return sum(A)