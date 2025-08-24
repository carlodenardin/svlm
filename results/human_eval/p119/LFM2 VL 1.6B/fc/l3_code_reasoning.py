def is_palindrome(s):
    i = 0
    c = len(s) - 1
    while i <= c:
        if s[i] != s[c]:
            return 'No'
        i += 1
        c -= 1
    return 'Yes'