# Declare a nested_extraction function that accepts a list and an index position.
#
# The function should use the index as the basic of finding both the nested list.
# and the element from that list with the given index position
#
# You can assume the number of lists will always be equal to
# the number of elements within each of them.
#
# nl = [[3,4,5],[7,8,9],[10,11,12]]
# nested_extracton (nl, 0)   => # 3
# nested_extracton (nl, 1)   => # 8
# nested_extracton (nl, 2)   => # 12

def nested_extraction(elements,index):
    return elements[index][index]

elements = [[3,4,5],[7,8,9],[10,11,12]]
print(nested_extraction(elements,0))


# Declare a beginning_and_end function that accepts a list of elements
#
# It should return True if the first and last elements in the list
#
# are equal and False if they are unequal.
#
# Assume the list will always have at least 1 element.
#
# beginning_and_end([1, 2, 3, 1])       => True 
# beginning_and_end([1, 2, 3, 4, 5])    => False
# beginning_and_end(["a", "b", "a"])    => True
# beginning_and_end([15])               => True

def beginning_and_end(elements):
    return elements[0] == elements[-1]

elements = ["a", "b", "a"]
print(beginning_and_end(elements))


# Declare a long_word_in_collection function that accepts a list and a string.
# The function should return True if
#   - the word exist in the list AND
#   - the word has more than 4 characters.
#
# words = ["cat", "dog", "rhino"]
# long_word_in_collection(words, "rhino")     => True
# long_word_in_collection(words, "cat")     => False
# long_word_in_collection(words, "monkey")     => False


def long_word_in_collection(words, string):
    return string in words and len(string) > 4


words = ["cat", "dog", "rhino"]
print(long_word_in_collection(words, "cat"))