# def multiply_by_one_less(numbers):
#     total = 0
#     for index, number in enumerate(numbers):
#         total += number * (index - 1)
#     return total

def multiply_by_one_less(numbers):
    total = 0
    for index, number in enumerate(numbers, -1):
        total += number * index
    return total

values = [1, 2, 3, 4, 5]

print(multiply_by_one_less(values))
