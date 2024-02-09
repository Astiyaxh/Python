def divisible_by_three_and_four(number):
    return number % 3 == 0 and number % 4 == 0

print(divisible_by_three_and_four(13))
print(divisible_by_three_and_four(14))
print(divisible_by_three_and_four(12))
print(divisible_by_three_and_four(18))
print(divisible_by_three_and_four(24))

def string_theory(string):
    return len(string)>3 and string[0] == "S"

print(string_theory("See"))
print(string_theory("Sansa"))
print(string_theory("Story"))
print(string_theory("Fable"))