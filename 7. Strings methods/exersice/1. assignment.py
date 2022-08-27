# Define a vowel_count function that accepts a string argument.
# The function should return the count of vowels in the string.
# The 5 vowles are "a", "e", "i", "o", and "u".
# You can assume the string will be in all lowercase.
#
# EXAMPLE:
# vowel_count("esrate")        => 3
# vowel_count("helicopter")    => 4
# vowel_count("ssh")           => 0
def vowel_count(text):
    return (text.count("a") + text.count("e") + text.count("i") + text.count("o") + text.count("u"))


print(vowel_count("helicopter"))
# Define a find_my_letter function that accepts two arguments: a string and a character
# The function should return the first index position of the character in the string
# The function should return a -1 if the character does not exist in the string
#
# EXAMPLES:
# find_my_letter("dangerous", "a")  => 1
# find_my_letter("bazooka", "z")    => 2
# find_my_letter("lollipop", "z")   => -1


def find_my_letter(word, character):
    return (word.find(character))


print(find_my_letter("lollipop", "z"))
