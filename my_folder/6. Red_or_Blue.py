print("Enter a number[1-2]: ", end='', flush=True)
number = int(input())
if number == 1:
    print("Red")
else:
    if number == 2:
        print("Blue")
    else:
        print("Invalid number")
