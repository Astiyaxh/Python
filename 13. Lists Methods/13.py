values = ["3.14", "9.99", "567.342", "5.678"]
print([value.split(".")[1] for value in values])
print([float(value) for value in values])

name = "Boris"
print([char*3 for char in name])


elements = ["Hydrogen", "Helium", "Lithium", "Boron", "Carbon"]
print([len(element) for element in elements])


def destroy_elements(list1, list2):
    return [element1 for element1 in list1 if element1 not in list2]


print(destroy_elements([1, 2, 3], [1, 2]))
print(destroy_elements([1, 2, 3], [1, 2, 3]))
print(destroy_elements([1, 2, 3], [4, 5]))

