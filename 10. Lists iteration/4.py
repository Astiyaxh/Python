def smallest_number(numbers):
    smallest = numbers[0]
    for number in numbers:
        if number < smallest:
            smallest = number
    return smallest

values = [3, 6, 9, 12, 15, 18, 21, 24]
print(smallest_number(values))

def concatenate(strings):
    concat = ""
    for string in strings:
        if len(string) > 2:
            concat += string
    return concat

print(concatenate(["abc", "def", "ghi", "ic"]))


def super_sum(strings):
    total = 0
    for string in strings:
        if "s" in string:
            total += string.find("s") # total += string.index("s")
    return total

print(super_sum([]))
print(super_sum(["mustache"]))
print(super_sum(["mustache", "greatest"]))
print(super_sum(["mustache", "pessimist"]))
print(super_sum(["mustache", "greatest", "almost"]))

