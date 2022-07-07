def add(a, b):
    print("The sum of", a, "and", b, "is", a + b)


add(4, 6)
add(a=4, b=6)
add(b=6, a=4)


def addd(a, b, c):
    print("The sum of the three numbers is", a + b + c)


addd(5, 10, 15)
addd(a=5, b=10, c=15)
addd(5, b=10, c=15)
addd(5, c=15, b=10)
