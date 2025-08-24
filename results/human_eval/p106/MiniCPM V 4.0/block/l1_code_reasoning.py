def generate_list(n: int):
    lst = [1]  # base for factorials starting from 1
    sum_factorials = 0  # sum of all previously computed factorials (for even indices)
    for i in range(1, n + 1):
        if i % 2 == 0:
            # compute i!
            fact = 1
            for k in range(2, i + 1):
                fact *= k
            lst.append(fact)
            sum_factorials += fact
        else:
            # append sum of previously computed factorials
            lst.append(sum_factorials)
    return lst

def main():
    n = int(input().strip())
    result = generate_list(n)
    print(result)

if __name__ == "__main__":
    main()