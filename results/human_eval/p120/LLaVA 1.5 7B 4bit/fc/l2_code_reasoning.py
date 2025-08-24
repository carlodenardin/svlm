from typing import Any, Dict, List, Callable
import math

def evaluate(node: Any, env: Dict[str, Any]=None) -> Any:
    """
    Evaluate an expression node.

    The expression should be provided as a nested dictionary structure with the following node types:
    - Literal: {'type': 'literal', 'value': <literal_value>}
    - Variable: {'type': 'var', 'name': <variable_name>}
    - Function call: {'type': 'call', 'name': <function_name>, 'args': [<arg_node>, ...]}
    - Operation: {'type': 'op', 'op': <operator_code>, 'left': <node>, 'right': <node>}
                 or {'type': 'op', 'op': 'NOT', 'expr': <node>} for unary NOT

    Operator codes (examples):
    - Arithmetic: 'ADD', 'SUB', 'MUL', 'DIV', 'MOD', 'POW'
    - Logical: 'AND', 'OR', 'NOT' (NOT is unary)
    - Comparisons: 'EQ', 'NE', 'LT', 'LE', 'GT', 'GE'

    Returns the evaluated value.
    """
    if env is None:
        env = {}
    if isinstance(node, (int, float, bool)):
        return node
    if isinstance(node, str) and (not isinstance(node, dict)):
        return node
    if not isinstance(node, dict) or 'type' not in node:
        raise TypeError(f'Invalid node: {node}')
    ntype = node['type']
    if ntype == 'literal':
        return node['value']
    if ntype == 'var':
        name = node['name']
        if name in env:
            return env[name]
        raise NameError(f'Unknown variable: {name}')
    if ntype == 'call':
        func_name = node['name']
        args_nodes: List[Any] = node.get('args', [])
        args = [evaluate(arg, env) for arg in args_nodes]
        if func_name in FUNC_REGISTRY:
            func = FUNC_REGISTRY[func_name]
            return func(*args)
        raise ValueError(f'Unknown function: {func_name}')
    if ntype == 'op':
        op = node['op']
        if op == 'NOT':
            expr_val = evaluate(node['expr'], env)
            return not bool(expr_val)
        if op in ('ADD', 'SUB', 'MUL', 'DIV', 'MOD', 'POW'):
            left = evaluate(node['left'], env)
            right = evaluate(node['right'], env)
            if op == 'ADD':
                return left + right
            if op == 'SUB':
                return left - right
            if op == 'MUL':
                return left * right
            if op == 'DIV':
                return left / right
            if op == 'MOD':
                return left % right
            if op == 'POW':
                return left ** right
        if op in ('AND', 'OR'):
            left = evaluate(node['left'], env)
            right = evaluate(node['right'], env)
            if op == 'AND':
                return bool(left) and bool(right)
            else:
                return bool(left) or bool(right)
        if op in ('EQ', 'NE', 'LT', 'LE', 'GT', 'GE'):
            left = evaluate(node['left'], env)
            right = evaluate(node['right'], env)
            if op == 'EQ':
                return left == right
            if op == 'NE':
                return left != right
            if op == 'LT':
                return left < right
            if op == 'LE':
                return left <= right
            if op == 'GT':
                return left > right
            if op == 'GE':
                return left >= right
        raise ValueError(f'Unknown operator: {op}')
    raise TypeError(f'Unsupported node type: {ntype}')