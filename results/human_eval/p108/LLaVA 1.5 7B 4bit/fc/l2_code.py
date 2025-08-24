def algorithm(diagram):
    logic = diagram.split(';')
    code = ''
    for i in range(len(logic)):
        code += f'if {logic[i]}:\n'
    return code