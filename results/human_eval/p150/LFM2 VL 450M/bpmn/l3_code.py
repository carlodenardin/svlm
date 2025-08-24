def process_input(numbers):
    if len(numbers) == 0:
        return 0
    elif len(numbers) == 1:
        return numbers[0]
    else:
        return sum(numbers[:len(numbers) - 1]) + numbers[len(numbers) - 1]