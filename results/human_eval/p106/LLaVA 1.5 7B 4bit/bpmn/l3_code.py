def algorithm(diagram):
    nodes = diagram.nodes()
    edges = diagram.edges()
    node_relations = {}
    for edge in edges:
        node1, node2 = (edge[0], edge[1])
        if node1 not in node_relations:
            node_relations[node1] = []
        if node2 not in node_relations:
            node_relations[node2] = []
        node_relations[node1].append(node2)
        node_relations[node2].append(node1)
    output = []
    for node, relations in node_relations.items():
        if len(relations) > 0:
            output_list = []
            for relation in relations:
                other_node = relation[0]
                output_list.append(get_output(diagram, other_node))
            output.append(output_list)
    return output