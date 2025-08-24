def algorithm(diagram):
    logic = diagram.split(';')
    code = ''
    for line in logic:
        code += line.strip() + '\n'
    return code