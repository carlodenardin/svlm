def solve():
    import sys

    def try_parse_number(tok):
        try:
            iv = int(tok)
            return ('int', iv)
        except Exception:
            pass
        try:
            fv = float(tok)
            return ('float', fv)
        except Exception:
            return None
    flowchart = '\nFlowchart: Overall Code\nStart\n  |\n  v\nRead the entire input as a single text block\n  |\n  v\nSplit input into lines; inspect the first line for numeric tokens\n  |\n  v\nAre there exactly two numeric tokens on the first line?\n  / \\\n  Yes  No\n  |     |\n  v     v\nCompute and print  Collect all numeric tokens from the entire input\nsum of those two    (numbers may be int or float)\nnumbers and return\n  |     \n  v\nEnd\n\nIf first line does not have exactly two numeric tokens:\n  |\n  v\nDo we have any numeric tokens anywhere in the input?\n  / \\\n  Yes  No\n  |     |\n  v     v\nSum all numeric tokens; Print  If any token is float, print as float; otherwise int\nas a number\n  |     \n  v\nEnd\n\nIf no numeric tokens exist anywhere:\n  |\n  v\nTake the entire input string, reverse it, print it\n  |\n  v\nEnd\n'
    text = sys.stdin.read()
    if text is None:
        text = ''
    text_stripped = text.rstrip('\n')
    if text is None or text.strip() == '':
        return
    lines = text.splitlines()
    first_line = lines[0] if lines else ''

    def numeric_tokens_in_line(line):
        toks = line.strip().split()
        nums = []
        kinds = []
        for t in toks:
            p = try_parse_number(t)
            if p is not None:
                kinds.append(p[0])
                nums.append(p[1])
        return (nums, kinds)
    nums_first, kinds_first = numeric_tokens_in_line(first_line)
    if len(nums_first) == 2:
        total = nums_first[0] + nums_first[1]
        if all((k == 'int' for k in kinds_first)) and total == int(total):
            print(int(total))
        else:
            print(total)
        return
    all_tokens = text.strip().split()
    numbers = []
    has_float = False
    for tok in all_tokens:
        p = try_parse_number(tok)
        if p is not None:
            kind, val = p
            numbers.append(val)
            if kind == 'float':
                has_float = True
    if len(numbers) > 0:
        total = sum(numbers)
        if not has_float and total == int(total):
            print(int(total))
        else:
            print(total)
        return
    print(text_stripped[::-1])
    return