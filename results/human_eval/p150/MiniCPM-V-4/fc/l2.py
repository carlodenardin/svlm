def x_or_y(n, x, y):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return y
    return x

print(x_or_y(7, 34, 12))  # Output: 34
print(x_or_y(15, 8, 5))   # Output: 5