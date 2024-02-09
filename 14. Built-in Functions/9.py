def greater_sum(first, second):
    return first if sum(first) > sum(second) else second


print(greater_sum([1, 2, 3], [1, 2, 4]))


def sum_difference(l1, l2):
    return sum(l1) - sum(l2)


print(sum_difference([1, 2, 3], [1, 2, 4]))