def algorithm(values):
    for i in range(1, len(values)):
        if values[i] == 'yes':
            return i * 0.25
        elif values[i] == 'no':
            return i * 0.75