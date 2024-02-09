def right_words(strings, limit):
    return len(strings) >= limit


strings = ["cat", "dog", "bean", "ace", "heart"]
limit = 4
print(list(filter(lambda word: len(word) == limit, strings)))

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
def only_odds(numbers):
    return (list(filter(lambda number: number % 2 != 0, numbers)))


def count_of_a(strings):
    return list(map(lambda string: string.count("a"), strings))


print(count_of_a(["alligator", "aardvark", "albatross"]))


