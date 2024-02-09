def word_lenghts(string):
    length_list = []
    each_word = string.split(" ")

    for word in each_word:
        length_list.append(len(word))

    return length_list

print(word_lenghts("Mary Poppins was a nanny"))




def cleanup(strings):
    clean_strings = []

    for string in strings:
        if string.isspace() or len(string) == 0:
            continue
        
        clean_strings.append(string)
        
    return " ".join(clean_strings)

print(cleanup(["cat", "er", "pillar"]))
print(cleanup(["cat", " ", "er", "", "pillar"]))
print(cleanup(["", "", " "]))