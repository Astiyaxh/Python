# Define a same-first-last-letter function that accepts a string as an argument.
# The function should return a True if the first and last character are equal,
# and False otherwise
# Assume the string will always have 1 or more characters.
#
# EXAMPLES:
# same-first-and-last-letter("runner")   => True
# same-first-and-last-letter("Runner")   => False
# same-first-and-last-letter("clock")    => False
# same-first-and-last-letter("q")        => True
def same_first_and_last_letter(word):
    return word[0] == word[-1]


print(same_first_and_last_letter("Runner"))
# Define a Three_number_sum function that accepts a 3-character string as an argument.
# The function should add up the sum of the digits of the string.
# HINT: You'll have to figure out a way to convert the string-ified numbers to intgers.
#
# EXAMPLES:
# three_number_sum("123")  => 6
# three_number_sum("567")  => 18
# three_number_sum("444")  => 12
# three_number_sum("000")  => 0


def three_number_sum(number):
    return int(number[0]) + int(number[1]) + int(number[2])


print(three_number_sum("123"))
