def first_and_last(mylist):
    return mylist[0] + mylist[-1]

print(first_and_last(["a", "b", "c"]))
print(first_and_last(["bob", "tom", "rob"]))
print(first_and_last(["a"]))

# def product_of_even_indices(mylist):
#     count = 0
#     total = 1
#     if len(mylist) == 6:
#         while count<=5:
#             if count % 2 == 0:
#                 total *= mylist[count]
#             count+=1
#         return total
#     else:
#         return "Enter a list with 6 elements!"
def product_of_even_indices(mylist):
    return mylist[0] * mylist[2] * mylist[4]

print(product_of_even_indices([1, 2, 3, 4, 5, 6]))
print(product_of_even_indices([3, 4, 3, 5, 3, 6]))


def first_letter_of_last_string(mylist):
    return mylist[-1][0]

print(first_letter_of_last_string(["cat", "dog", "zebra"]))