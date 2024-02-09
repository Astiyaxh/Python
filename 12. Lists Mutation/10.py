def factor(number):
    num_list = []
    rng = range(1, number + 1)

    for i in rng:
        if number % i == 0:
            num_list.append(i)
    return num_list

print(factor(10))

