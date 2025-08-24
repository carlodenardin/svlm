def algorithm(diagram):
    logic = diagram.split(';')
    code = ''
    for i in range(len(logic)):
        code += f'{logic[i]}\n'
    return code