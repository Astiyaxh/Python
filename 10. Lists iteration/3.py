values = [3, 6, 9, 12, 15, 18, 21, 24]
other_values = [5, 10, 15, 20, 25, 30]
def odds_sum(mylist):
    total = 0
    for number in mylist:
        if number % 2 == 1:
            total += number
    print(total)

odds_sum(values)
odds_sum(other_values)


def greatest_number(mylist):
    greatest = mylist[0]
    for number in mylist:
        if number > greatest:
            greatest = number
    return greatest


print(greatest_number([1, 2, 3]))
print(greatest_number([3, 2, 1]))
print(greatest_number([4, 5, 5]))
print(greatest_number([-3, -2, -1]))