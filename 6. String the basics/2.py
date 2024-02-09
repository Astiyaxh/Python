def long_word(word):
    return len(word) > 7

print(long_word("Hello, World!"))


def first_longer_than_second(first, second):
    return len(first) > len(second)

print(first_longer_than_second("Hello", "Hell yah!"))