def first_three_characters(string):
    return string[:3]

print(first_three_characters("Hello"))

def last_five_characters(string):
    return string[-5:]

print(last_five_characters("empire"))


def is_palindrome(string):
    return string == string[::-1]

print(is_palindrome("racecar"))