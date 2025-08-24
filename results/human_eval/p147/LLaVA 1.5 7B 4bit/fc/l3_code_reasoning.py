def count_yes_no_sentences(text):
    t = text.lower()
    yes_count = 0
    no_count = 0
    for i in range(len(t)):
        if i + 3 <= len(t) and t[i:i + 3] == 'yes':
            yes_count += 1
        if i + 2 <= len(t) and t[i:i + 2] == 'no':
            no_count += 1
    return (yes_count, no_count)