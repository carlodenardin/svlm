def generate_function(input_value):
    list_of_n = []
    for i in range(1, input_value + 1):
        list_of_n.append(i * i - i + 1)
    return len(list_of_n) % 3 == 0