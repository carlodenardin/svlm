def count_multiples_of_3_in_triples(n):
    A = [i * i - i + 1 for i in range(1, n + 1)]
    counter = 0
    for i in range(n - 2):
        triple_sum = A[i] + A[i + 1] + A[i + 2]
        if triple_sum % 3 == 0:
            counter += 1
    return counter