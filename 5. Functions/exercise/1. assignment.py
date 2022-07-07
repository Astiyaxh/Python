# Define a easy_money function that accepts no parameters
# and always returns the value 100.
def easy_money():
    return 100


result = easy_money()
print(result)


# Define a best_food_ever function that accepts
# no parameters and always returns the string "kabab koobideh"
def best_food_ever():
    return "kabab koobideh"


result = best_food_ever()
print(result)


# Define a convert_to_currency function that accepts a single parameters (an interger)
# The function should convert the argument to a string,
# prefix it with a dollar sign, and return the result.
#
# EXAMPLES:
# convert_to_currency(15) => "$15"
# convert_to_currency(8)  => "$8"
def convert_to_currency(a):
    return "$" + str(a)


result = convert_to_currency(25)
print(result)
