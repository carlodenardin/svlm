def count_even_and_odd_digits():
    count = 0
    for i in range(10):
        if i % 2 == 0:
            count += 1
        else:
            count += 0
    return count