def process_data(data):
    k = data[0]
    for i in range(1, len(data)):
        if data[i] == k:
            return k
    return None