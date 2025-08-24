def check_numbers(numbers, diagram):
    for number in numbers:
        if number not in diagram:
            print(f'{number} is not in the diagram')
        else:
            print(f'{number} is in the diagram')