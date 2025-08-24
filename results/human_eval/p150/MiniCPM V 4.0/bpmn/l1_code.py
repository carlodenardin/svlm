def process_input(n, x, y):
    if is_prime(n):
        return x
    else:
        return y

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Example usage:
n = 7  # Replace with the input value for n
x = 10  # Replace with the initial value of x
y = 20  # Replace with the initial value of y
result = process_input(n, x, y)
print(result)  # Output will be '10' or '20' based on whether n is prime or not