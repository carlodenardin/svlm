def count_integers(numbers):
    counter = 0
    for _ in numbers:
        if counter > 0:
            counter += 1
    return counter