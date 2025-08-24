def process_input(input):
    count = 0
    while True:
        input = input.split()
        if len(input) == 1:
            count += 1
        else:
            return count