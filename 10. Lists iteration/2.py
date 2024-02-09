def sum_of_lengths(mylist):
    total = 0
    for element in mylist:
        total += len(element)
    return total

print(sum_of_lengths(["Hello", "Bob"]))
print(sum_of_lengths(["Nonsense"]))
print(sum_of_lengths(["Nonsense", "or", "confidence"]))


def myproduct(mylist):
    total = 1
    for value in mylist:
        total *= value
    return total

print(myproduct([1, 2, 3]))
print(myproduct([4, 5, 6, 7]))
print(myproduct([10]))

