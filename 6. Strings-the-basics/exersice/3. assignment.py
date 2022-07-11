# Define a first-three-characters function that accepts a string argument.
# The function should return the first 3 characters of the string.
#
# EXAMPLES:
# first_three_characters("dynasty")  =>"dyn"
# first_three_characters("empire")   =>"emp"
def first_three_characters(word):
    return word[:3]


print(first_three_characters("dynasty"))

# Define a last-five-characters function that accepts a string argument.
# The function should return the last 5 characters of the string.
#
# EXAMPLES:
# last_five_characters("dynasty") => "nasty"
# last_five_characters("empire") => "mpire"


def first_three_characters(word):
    return word[-5:]


print(first_three_characters("dynasty"))


# Define a is_palindrome function that accepts a string argument.
# The function should return True if the string is spelled
# the same backwards as it is forwards.
# Return False otherwise.
#
# EXAMPLE:
# is-palindrome("racecar")  => True
# is-palindrome("yummy")  => False
def is_palindrome(string):
    return string == string[::-1]


print(is_palindrome("racecar"))
