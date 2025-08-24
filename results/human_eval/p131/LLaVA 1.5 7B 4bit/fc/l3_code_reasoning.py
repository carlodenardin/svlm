def evaluate_expression(expr):
    """
    Evaluate an expression represented as:
    - numbers (int/float/bool)
    - dict with keys: 'op', 'left', 'right'
      op in {'+', '-', '*', '/', '**', 'and', 'or'}
    The function recursively evaluates sub-expressions following the described approach:
    - If the expression is a raw number/bool, return it.
    - If the expression is an operator node, evaluate its sub-expressions and apply the operator.
      For arithmetic operators, return numeric results.
      For 'and'/'or', return boolean results.
    """
    if isinstance(expr, (int, float, bool)):
        return expr
    if isinstance(expr, dict):
        op = expr.get('op')
        left = evaluate_expression(expr.get('left'))
        if op in ('and', 'or'):
            right = evaluate_expression(expr.get('right'))
            if op == 'and':
                return bool(left) and bool(right)
            else:
                return bool(left) or bool(right)
        else:
            right = evaluate_expression(expr.get('right'))
            if op == '+':
                return left + right
            elif op == '-':
                return left - right
            elif op == '*':
                return left * right
            elif op == '/':
                return left / right
            elif op == '**':
                return left ** right
            else:
                raise ValueError(f'Unsupported operator: {op}')
    raise TypeError('Unsupported expression type')