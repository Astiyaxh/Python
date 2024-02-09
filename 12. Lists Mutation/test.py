number = 13649
number_length = len(str(number))
print(number_length)
holder = []
for i in range(0,5):
    holder.append(number % 10)
    number = int(number / 10)

print(holder)
