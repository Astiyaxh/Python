def in_list(strings, target):
    for index, string in enumerate(strings):
        if string == target:
            return index
        
    return -1

strings = ["enchanted", "sparks fly", "long live"]
print(in_list(strings, "enchanted"))
print(in_list(strings, "sparks fly"))
print(in_list(strings, "fifteen"))
print(in_list(strings, "live story"))
print(in_list(strings, "long live"))


def sum_of_values_and_indices(numbers):
    total = 0
    for index, number in enumerate(numbers):
        total += index + number

    return total


print(sum_of_values_and_indices([1, 2, 3]))
print(sum_of_values_and_indices([0, 0, 0, 0]))
print(sum_of_values_and_indices([]))