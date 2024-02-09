def same_first_and_last_letter(string):
    return string[0] == string[-1]

print(same_first_and_last_letter("runner"))
print(same_first_and_last_letter("Runner"))
print(same_first_and_last_letter("clock"))
print(same_first_and_last_letter("q"))


def three_number_sum(string):
    if len(string) > 3 or len(string) < 3:
        return "try again!"
    else:
        return int(string[0]) + int(string[1]) + int(string[2])

print(three_number_sum("125"))
