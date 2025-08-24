def algorithm(diagram):
    logic = diagram.split(';')
    code = ''
    for line in logic:
        code += f'{line}\n'
    return code