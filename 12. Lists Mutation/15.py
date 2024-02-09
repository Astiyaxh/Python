def delete_all(strings, target):
    while target in strings:
        strings.remove(target)
    return strings

print(delete_all([1, 3, 3, 5], 3))


def push_or_pop(numbers):
    result = []
    for number in numbers:
        if number > 5:
            result.append(number)
        else:
            result.pop()
    return result

print(push_or_pop([10, 20, 2, 30]))