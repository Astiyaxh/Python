# def reverse(string):
#     start_index = 0
#     last_index = len(string) - 1
#     reversed_string = ""
#     while last_index >= start_index :
#         reversed_string += string[last_index]
#         last_index-=1
#     print(reversed_string)

def reverse(string):
    if len(string) <= 1:
        return string
    
    return string[-1] + reverse(string[0:-1])


print(reverse("Hello"))

# Hello
# H + reverse(ello)
# H + e + reverse(llo)
# H + e + l + reverse(lo)
# H + e + l + l + reverse(o)
# H + e + l + l + o