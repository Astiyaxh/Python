mountains = ["Mount Everest", "K2"]
print(mountains)

mountains.extend(["Kangchenjunga", "Lhotse", "Makalu", "Damavand"])
print(mountains)

extra_mountains = ["Cho Oya", "Dhaulagiri"]
mountains.extend(extra_mountains)
print(mountains)


steaks = ["Tenderloin", "New York Strip"]
more_steaks = ["T-Bone", "Ribeye"]

my_meal = steaks + more_steaks
print(my_meal)