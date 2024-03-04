students = ["Bob", "Sally", "Sue"]
athletes = students
nerds = ["Bob", "Sally", "Sue"]

print(students == athletes)
print(students == nerds)

print(students is athletes)
print(students is nerds) # they have the same value but they don't have same object!

a = 1
b = 1
print(a == b)
print(a is b)

a = 3.14
b = 3.14
print(a == b)
print(a is b)

a = "hello"
b = "hello"
print(a == b)
print(a is b)

