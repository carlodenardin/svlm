def receive_integer():
    # Receive the integer input from the user
    n = int(input("Enter an integer: "))
    return n

def is_odd(n):
    # Check if the integer is odd
    return n % 2 != 0

def compute_product(n):
    # Compute the product of the odd digits
    product = 1
    for digit in str(n):
        if digit.isdigit() and int(digit) % 2 != 0:
            product *= int(digit)
    return product

def main():
    # Main function to run the algorithm
    n = receive_integer()
    if is_odd(n):
        return 0
    else:
        return compute_product(n)

if __name__ == "__main__":
    result = main()
    print(result)