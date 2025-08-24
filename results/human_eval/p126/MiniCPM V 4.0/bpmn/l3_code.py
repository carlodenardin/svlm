def check_palindrome(list):
    i = 1
    while i < len(list):
        if list[i] < list[i - 1]:
            return False
        elif i > 1 and list[i] == list[i - 1] == list[i - 2]:
            return False
        i += 1
    return True