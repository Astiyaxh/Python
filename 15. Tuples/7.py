def accept_stuff(*args):
    print(type(args))
    print(args)
    
accept_stuff()
accept_stuff(1)
accept_stuff(1, 2, 3)
accept_stuff(1, 2, 3, 4 ,5)


def my_max(nonsense, *numbers):
    print(nonsense)
    greatest = numbers[0]
    for number in numbers:
        if number > greatest:
            greatest = number
    return greatest

print(my_max("Shazam", 1))
print(my_max("Hoorah", 1, 3))
print(my_max("Bonanaza", 1, 3, 9, -6, -12, 4, 5, 6, 1))


def my_max(*numbers, nonsense):
    print(nonsense)
    greatest = numbers[0]
    for number in numbers:
        if number > greatest:
            greatest = number
    return greatest


print(my_max(1, nonsense= "Shazam"))
print(my_max(1, 3, nonsense="Hoorah"))
print(my_max(1, 3, 9, -6, -12, 4, 5, 6, 1, nonsense="Bonanaza"))