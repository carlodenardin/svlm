def balanced_strings(list_of_strings):
    concatenated = ''.join(list_of_strings)
    balanced = all((c == c for c in concatenated))
    if balanced:
        return 'Yes'
    else:
        return 'No'