counter = 0
print("Enter number-1: ", end='', flush=True)
num1 = int(input())
if num1 % 2 == 0:
    counter = counter + 1
print("Enter number-2: ", end='', flush=True)
num2 = int(input())
if num2 % 2 == 0:
    counter = counter + 1
print("Enter number-3: ", end='', flush=True)
num3 = int(input())
if num3 % 2 == 0:
    counter = counter + 1
print("Enter number-4: ", end='', flush=True)
num4 = int(input())
if num4 % 2 == 0:
    counter = counter + 1
print("Enter number-5: ", end='', flush=True)
num5 = int(input())
if num5 % 2 == 0:
    counter = counter + 1
print("Count of Even numbers is " + str(counter))
