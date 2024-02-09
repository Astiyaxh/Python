def split_in_two(mylist, number):
    if number % 2 == 0:
        return mylist[2:]
    else:
        return mylist[:2]

values = ["a", "b", "c", "d", "e", "f"]
print(split_in_two(values, 3))
print(split_in_two(values, 4))
print(split_in_two(values, 1))
print(split_in_two(values, 10))
