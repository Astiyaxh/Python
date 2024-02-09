powerball_numbers = [4, 8, 15, 16, 23, 42]

# def squares(numbers):
#     results = []
#     for number in numbers:
#         number *= number
#         results.append(number)
#     return results

def squares(numbers):
    squares = []
    for number in numbers:
        squares.append(number ** 2)
    return squares

print(squares(powerball_numbers))



def convert_to_floats(numbers):
    float_list = []
    for number in numbers:
        float_list.append(float(number))
    return float_list

print(convert_to_floats(powerball_numbers))


def even_or_odd(numbers):
    true_or_false = []
    for number in numbers:
        if number % 2 == 0:
            true_or_false.append(True)
        else:
            true_or_false.append(False)
    return true_or_false

print(even_or_odd(powerball_numbers))
