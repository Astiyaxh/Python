# # sum of all digits in list
# numbers = [1, 5, 4, 6, 7]
# def sum_of_all(numbers):
#     total = 0
#     for number in numbers:
#         total += number
#     return total

# print(sum_of_all(numbers))

# # Calculate uppercase and lowecase in string
# string = "HeLLo"
# upper = 0
# lower = 0
# for s in string:
#     if s.isupper():
#         upper += 1
#     else:
#         lower += 1
# print("Uppercase:", upper, "Lowercase:", lower)

# def count_upper_lower(text):
#     upper_count = 0
#     lower_count = 0
    
#     for char in text:
#         if char.isupper():
#             upper_count += 1
#         elif char.islower():
#             lower_count += 1
    
#     return f"upper:{upper_count}", f"lower:{lower_count}"

# print(count_upper_lower("HeLLo"))



# def min_and_max(items):
#     max = items[0]
#     min = items[0]
#     for item in items:
#         if item > max:
#             max = item
#         elif item < min:
#             min = item
#     return f"Max is {max} and Min is {min}"


# print(min_and_max([1, 3, 5, 64, 3, 0, -1]))

# print('Hello'[::-1])


def average(items):
    return sum(items) / len(items)

print(average([1, 3, 5]))


def word_count(items):
    for item in items:
        items.count(item)