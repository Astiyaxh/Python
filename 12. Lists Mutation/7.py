def only_evens(numbers):
    evens = []
    for number in numbers:
        if number % 2 == 0:
            evens.append(number)
    return evens

print(only_evens([4, 8 , 15, 16, 23, 42]))
print(only_evens([1, 3, 5]))
print(only_evens([]))



def long_strings(strings):
    result = []
    for string in strings:
        if len(string) >= 5:
            result.append(string)
    return result

print(long_strings(["Hello", "Goodbye", "Sam"]))
print(long_strings(["Ace", "Cat", "Job"]))
print(long_strings([]))