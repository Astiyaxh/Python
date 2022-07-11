# Define a long_word function that accepts a string
# The function should return a Boolean that reflects
# whether the string has more than 7 characters
#
# EXAMPLES:
# long_word("Python")       => false
# long_word("magnificent")  => True
def long_word(word):
    return (len(word) >= 7)


print(long_word("magnificent"))

# Define a first_longer_than_second function that accepts two string arguments.
# The function should return a True if the first string is linger than the second
# and False otherwise (including if they are equal in length).
#
# EXAMPLES:
# First_longer_than_second("python","Ruby")       =>True
# First_longer_than_second("cat","mouse")         =>False
# First_longer_than_second("Steven","Seagal")     =>False

def First_longer_than_second(word_1, word_2):
    return len(word_1) > len(word_2)


print(First_longer_than_second("Steven", "Seagal"))