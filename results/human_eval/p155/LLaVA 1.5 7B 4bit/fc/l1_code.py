def count_even_and_odd_digits_in_n():
    n = int(input('Enter a number: '))
    count = 0
    for i in range(n):
        if i % 2 == 0:
            count += 1
        else:
            count += 2
    print('Number of even digits:', count)