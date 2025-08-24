def check_prime(n, x, y):
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def main():
    n = int(input("Enter a number: "))
    x = None
    y = None

    if check_prime(n, x, y):
        print("Yes")
    else:
        print("No")

main()