def positive_or_negative(number):
    if number > 0:
        return "Positive!"
    elif number < 0:
        return "Negative!"
    else:
        return "Neither! It's zero"


print(positive_or_negative(-9))
print(positive_or_negative(10))
print(positive_or_negative(0))
print(positive_or_negative(3))
print(positive_or_negative(-13))


def calculator(operation, a, b):
    if operation == "add":
        return a + b
    elif operation == "sub":
        return a - b
    elif operation == "mul":
        return a * b
    elif operation == "div":
        return a / b
    else:
        return "I don't know what you want me to do!"


print(calculator("add",3,4))
print(calculator("sub",3,4))
print(calculator("mul",3,4))
print(calculator("div",3,4))
print(calculator(" ",3,4))
print(calculator("transmogrify",3,4))