def even_or_odd(integer):
    if integer % 2 == 0:
        return "even"
    else:
        return "odd"

print(even_or_odd(11))


def truthy_or_falsy(arg):
    if arg:
        return f"The value {arg} is truthy"
    else:
        return f"The value {arg} is falsy"

print(truthy_or_falsy(10))
print(truthy_or_falsy(0))
print(truthy_or_falsy(""))
print(truthy_or_falsy("hello"))