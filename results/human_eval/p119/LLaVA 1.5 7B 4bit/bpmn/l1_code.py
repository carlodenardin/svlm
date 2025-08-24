def balance(strings):
    list = strings.split(';')
    for i in range(len(list)):
        if list[i] == 'no':
            return 'no'
        elif list[i] == 'yes':
            return 'yes'
    return 'no'