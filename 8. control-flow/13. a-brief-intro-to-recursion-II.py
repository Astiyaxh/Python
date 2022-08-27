# def reverse(string):
#     start_index = 0
#     last_index = len(string) - 1
#     reverse_string = ""

#     while last_index >= start_index:
#         reverse_string += string[last_index]
#         last_index -= 1

#     return reverse_string

def reverse(string):              
    if len(string) <= 1:
        return string

    return string[-1] + reverse(string[:-1])

print(reverse("reza")) #warts

# straw 
# w + reverse(stra)
# w + a + reverse(str)
# w + a + r + reverse(st)
# w + a + r + t + reverse(s)
# w + a + r + t + s