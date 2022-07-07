# Define a string_adder function that accepts two string (a and b) as arguments.
# It should return a concatenated version of the arguments with a space in between.
# if the user does not pass in arguments, both arguments should default to an empty string.
#
# EXAMPLES
# string_adder("Hello", "World")     => "Hello World"
# string_adder("Emillio", "Estevez") => "Emilio Estevez"
# string_adder()                     => " "
# string_adder("Tiger")              => "Tiger "


def string_adder(a="", b=""):
    return a + " " + b


print(string_adder("Cyrus", "The Great"))


# Define a multiplier function that accepts three integers as arguments
# Return the product of the arguments.
# The product is the total when values are multiplied together.
# If the user does not provide any arguments, all three parameters
# should heve default arguments of 1.
#
# EXAMPLES
# multiplier(2, 2, 2)       => 8
# multiplier()              => 1
# multiplier(3)             => 3
# multiplier(2, 5)          => 10


def multiplier(a=1, b=1, c=1):
    return a * b * c


print(multiplier(10, 20, 30))
