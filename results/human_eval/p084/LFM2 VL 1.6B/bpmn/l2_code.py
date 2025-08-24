def receive_integer():
    # Receive the integer number from the user
    number = int(input("Enter an integer number: "))
    return number

def initialize_variables():
    # Initialize two variables, sum and res, to zero
    sum = 0
    res = 0
    return sum, res

def compute_sum(number, sum):
    # Compute the sum of the digits of the integer number
    n = abs(number)
    while n > 0:
        digit = n % 10
        sum += digit
        n //= 10
    return sum

def convert_to_binary(sum_value):
    # Convert the sum to binary representation
    binary = bin(sum_value)
    return binary

def solve():
    number = receive_integer()
    sum, res = initialize_variables()
    sum = compute_sum(number, sum)
    res = convert_to_binary(sum)
    return res

if __name__ == "__main__":
    result = solve()
    print(result)