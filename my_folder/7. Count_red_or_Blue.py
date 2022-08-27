rcounter = 0
bcounter = 0
icounter = 0
print("User-1 please Enter a number[1-2]: ")
number = int(input())
if number == 1:
    rcounter = rcounter + 1
else:
    if number == 2:
        bcounter = bcounter + 1
    else:
        icounter = icounter + 1
print("User-2 please Enter a number[1-2]: ")
number = int(input())
if number == 1:
    rcounter = rcounter + 1
else:
    if number == 2:
        bcounter = bcounter + 1
    else:
        icounter = icounter + 1
print("User-3 please Enter a number[1-2]: ")
number = int(input())
if number == 1:
    rcounter = rcounter + 1
else:
    if number == 2:
        bcounter = bcounter + 1
    else:
        icounter = icounter + 1
print("User-4 please Enter a number[1-2]: ")
number = int(input())
if number == 1:
    rcounter = rcounter + 1
else:
    if number == 2:
        bcounter = bcounter + 1
    else:
        icounter = icounter + 1
print("User-5 please Enter a number[1-2]: ")
number = int(input())
if number == 1:
    rcounter = rcounter + 1
else:
    if number == 2:
        bcounter = bcounter + 1
    else:
        icounter = icounter + 1
print("Red is " + str(rcounter))
print("Blue is " + str(bcounter))
print("Invalid votes is " + str(icounter))
