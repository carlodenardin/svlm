def algorithm(diagram):
    nodes = diagram.nodes()
    edges = diagram.edges()
    state = {}
    for node in nodes:
        state[node] = [False] * len(edges)
    for node in nodes:
        state[node][0] = True
    for edge in edges:
        for i in range(len(edge)):
            from_node = edge[i]
            to_node = edge[i + 1]
            if state[from_node][i] and state[to_node][i]:
                state[from_node][i] = False
                state[to_node][i] = True
    return state