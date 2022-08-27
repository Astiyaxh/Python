# Define a divisible_by_three_and_four function that accepts a number as its argument.
# It should return True if the number is evenly divisible by both 3 and 4
# It should return False otherwise.
#
# divisible_by_Three_and_four(3)    => False
# divisible_by_Three_and_four(4)    => False
# divisible_by_Three_and_four(12)   => Ture
# divisible_by_Three_and_four(18)   => False
# divisible_by_Three_and_four(24)   => Ture

def divisible_by_three_and_four(number):
    return number % 3 == 0 and number % 4 == 0

print(divisible_by_three_and_four(13))


# Declare a string_theory function  that accepts a string as an argument.
# It should return True if the string has more than 3 character 
# and starts with a capital "S". It should return False otherwise.
#
# string_thoery("Sansa")  => True
# string_thoery("Story")  => True
# string_thoery("See")  => False
# string_thoery("Fable")  => False

def string_thoery(string):
    return len(string) > 3 and string[0] == "S"

string_thoery("Fable")