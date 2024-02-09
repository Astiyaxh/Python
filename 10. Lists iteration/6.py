errands = ["Go to gym", "Grab lunch", "Get promoted at work", "Sleep"]

print(enumerate(errands))

for index, errand in enumerate(errands, 1):
    print(f"{errand} is number {index} on my list of things to do today!")
    
# for idx, task in enumerate(errands):
#     print(f"{task} is number {idx} on my list of things to do today!")

# for index, errand in enumerate(errands):
#     print(f"{errand} is number {index+1} on my list of things to do today!")