def generate_function():

    def generate():
        i = 0
        while i <= n:
            if i == n:
                return
            i += 1
            x = i
            j = 1
            while j <= i:
                if j == i:
                    return
                j += 1
                x += j
            return
    return generate