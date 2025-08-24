def algorithm(diagram):
    nodes = diagram.split(';')
    connections = {}
    for node in nodes:
        name, value = node.split('=')
        connections[name] = value
    return connections