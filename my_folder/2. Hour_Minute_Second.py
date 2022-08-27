print("Enter Hour: ")
h = int(input())
print("Enter Minute: ")
m = int(input())
print("Enter Second: ")
s = int(input())
t = h * 3600
t = t + m * 60
t = t + s
print("Total: " + str(t))
