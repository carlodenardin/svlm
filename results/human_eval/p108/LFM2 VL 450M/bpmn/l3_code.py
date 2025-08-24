def process_integers(iterable):
    for element in iterable:
        if element == 'yes':
            return element
        elif element == 'no':
            return None
        else:
            return element