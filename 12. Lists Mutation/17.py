temperatures = [40, 28, 52, 66, 35]
temperatures.sort()
temperatures.reverse()
print(temperatures)

coffees = ["Latte", "Espresso", "Macchiato", "Frappucino"]
coffees.sort()
coffees.reverse()
print(coffees)

# capital letter sorts first
coffees = ["Latte", "espresso", "macchiato", "Frappucino"] 
coffees.sort()
coffees.reverse()
print(coffees)

# That way, it doesn't affect the original data and gets a copy of data
coffees = ["Latte", "Espresso", "Macchiato", "Frappucino"]
print(sorted(coffees))