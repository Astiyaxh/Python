# Define a first_and_last function that accepts a list of string.
# The function should return a concatenation of the first element and last element.
# Assume the list will always have 1 or more elements.
#
# first_and_last(["a", "b", "c"])       => "ac"
# first_and_last(["bob", "tom", "rob"]) => "bobrob"
# first_and_last(["a"])                 => "aa"
def first_and_last(elements):
    return elements[0] + elements[-1]

elements = ["bob", "tom", "rob"]
print(first_and_last(elements))

# Define a product_of_even_indices function that accepts a list of number.
# The list will always have 6 total elements.
# The function should return the product (multiplied total)
# of all number at an even index (0, 2, 4).
#
# product_of_even_indices([1, 2, 3, 4, 5, 6])  => 15
# product_of_even_indices([3, 4, 3, 5, 3, 6])  => 27

def product_of_even_indices(numbers):
    return numbers[0] * numbers[2] * numbers[4]

numbers = [3, 4, 3, 5, 3, 6]
print(product_of_even_indices(numbers))

# Define a first_letter_of_last_string function that accepts a list of strings.
# It should return one character - the first letter of the last string in the list.
# Assume the list will always have at least one string.
#
# first_letter_of_last_string(["cat", "dog", "zebra"])  => "z"
# first_letter_of_last_string(["nonsense"])             => "n"

def first_letter_of_last_string(elements):
    return elements[-1][0]


elements = ["cat", "dog", "zebra"]
print(first_letter_of_last_string(elements))