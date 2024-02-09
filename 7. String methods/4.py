def vowel_count(string):
    return string.count("a") + \
           string.count("e") + \
           string.count("i") + \
           string.count("o") + \
           string.count("u")

print(vowel_count("Hello")) 


def find_my_letter(string, char):
    return string.find(char)

print(find_my_letter("bazooka", "z"))
print(find_my_letter("bazooka", "x"))