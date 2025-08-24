def process_strings(combinations):
    for combination in combinations:
        if combination[0] == '1':
            if combination[1] == '2':
                return 'Concat the 2 string with both the combinations'
            else:
                return 'Check if at least one string is balanced?'
        else:
            return 'Balanced means that every "1" has a matching; and closes never exec opens order'