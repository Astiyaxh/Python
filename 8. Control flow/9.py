if 5 < 7 and "rain" == "rain":
    print("Both of those conditions evaluate to true")
if 5 < 7 and "rain" == "fier":
    print("This will not print beacause at least one of the two conditions is false")
if "rain" == "fire" and 5 < 7:
    print("This will not print beacause at least one of the two conditions is false")
if "rain" == "fire" and 5 < 3:
    print("This will not print beacause at least one of the two conditions is false")

value = 95

# if value > 90 and value < 100:
if 90 < value < 100:
    print("This is a shourtcut for the win!")
