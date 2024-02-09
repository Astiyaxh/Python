# def nested_extraction(lol, index):
#     if index == 0:
#         return lol[0][0]
#     elif index == 1:
#         return lol[1][1]
#     return lol[2][2]
def nested_extraction(lol, index):
    return lol[index][index]

nl = [[3, 4, 5], [7, 8, 9], [10, 11, 12]]
print(nested_extraction(nl, 0))
print(nested_extraction(nl, 1))
print(nested_extraction(nl, 2))

def beginning_and_end(mylist):
    return mylist[0] == mylist[-1]

print(beginning_and_end([1, 2, 4, 1]))
print(beginning_and_end([1, 2, 4, 5, 2]))


def long_word_in_collection(mylist, string):
    return string in mylist and len(string) > 4

words = ["cat", "dog", "rhino"]
print(long_word_in_collection(words, "rhino"))
print(long_word_in_collection(words, "cat"))
print(long_word_in_collection(words, "monkey"))
