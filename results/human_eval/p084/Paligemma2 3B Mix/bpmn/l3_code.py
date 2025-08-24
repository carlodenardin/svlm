from typing import Any, Dict, Optional
import re
import math

def solve_vlm_problem(problem_text: str, image_caption: Optional[str]=None) -> Dict[str, Any]:
    """
    This function attempts to follow a simple, generic reasoning pattern that a tiny VLM might use
    to solve arithmetic-like problems described in text (and optionally referencing an image caption).
    It handles:
    - Simple binary expressions like '3 + 4' or '12.5 * 2'
    - Factorial expressions like 'factorial of 5'
    - Square roots like 'sqrt of 16'
    - Phrasal sums like 'sum of 3 and 4'
    If nothing matches, it returns a dictionary with answer=None.
    """
    s = problem_text.strip()
    m = re.search('(-?\\d+(?:\\.\\d+)?)\\s*([+\\-*/])\\s*(-?\\d+(?:\\.\\d+)?)', s)
    if m:
        a = float(m.group(1))
        op = m.group(2)
        b = float(m.group(3))
        res = None
        if op == '+':
            res = a + b
        elif op == '-':
            res = a - b
        elif op == '*':
            res = a * b
        elif op == '/':
            res = a / b if b != 0 else None
        return {'answer': res, 'method': 'binary_expression', 'text': s, 'image_caption': image_caption}
    m = re.search('factorial\\s*(?:of)?\\s*(-?\\d+)', s.lower())
    if m:
        n = int(m.group(1))
        if n < 0:
            return {'answer': None, 'method': 'factorial', 'text': s, 'image_caption': image_caption, 'error': 'negative_input'}
        return {'answer': math.factorial(n), 'method': 'factorial', 'n': n, 'text': s, 'image_caption': image_caption}
    m = re.search('sqrt(?: of)?\\s*(-?\\d+(?:\\.\\d+)?)', s.lower())
    if m:
        n = float(m.group(1))
        if n < 0:
            return {'answer': None, 'method': 'sqrt', 'text': s, 'image_caption': image_caption, 'error': 'negative_input'}
        return {'answer': math.sqrt(n), 'method': 'sqrt', 'n': n, 'text': s, 'image_caption': image_caption}
    m = re.search('sum\\s*(?:of)?\\s*(-?\\d+(?:\\.\\d+)?)\\s*(?:and|,)\\s*(-?\\d+(?:\\.\\d+)?)', s.lower())
    if m:
        a = float(m.group(1))
        b = float(m.group(2))
        return {'answer': a + b, 'method': 'sum_phrase', 'a': a, 'b': b, 'text': s, 'image_caption': image_caption}
    return {'answer': None, 'text': s, 'image_caption': image_caption}