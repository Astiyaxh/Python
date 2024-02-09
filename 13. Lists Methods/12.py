# print(["abcdefghijklmnopqrstuvwxyz".index(char) for char in "donut"])

# print([number / 2 for number in range(20)])

donuts = [
    "Boston Cream",
    "Jelly",
    "Vanilla Cream",
    "Glazed",
    "Chocolate Cream"
]
# print([donut for donut in donuts if "Cream" in donut])

# print([(donut,len(donut)) for donut in donuts if "Cream" in donut ])

print([donut.split(" ")[0] for donut in donuts if "Cream" in donut])