def evaluateExpression(x, y):
    if x != 1:
        return evaluateExpression(x + y)
    else:
        return y