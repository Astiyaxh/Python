def positive_or_negative(number):
    if number > 0:
        return "Positive!"
    elif number < 0:
        return "Negative!"
    else:
        return "Neither! It's zero"

print(positive_or_negative(0))
print(positive_or_negative(-10))
print(positive_or_negative(10))


def calculator(operation, a, b):
    if operation == "add":
        return a + b
    elif operation == "subtract":
        return a - b
    elif operation == "mulyiply":
        return a * b
    elif operation == "divide":
        return a / b
    else: 
        return f"I don't know what the fuck is the \"{operation}\" doing get lost!"

print(calculator("add", 3, 4))
print(calculator("subtract", 3, 4))
print(calculator("mulyiply", 3, 4))
print(calculator("divide", 3, 4))
print(calculator("nonesence", 3, 4))