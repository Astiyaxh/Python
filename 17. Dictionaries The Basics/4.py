pokemon = {
    "Fire": ["Charmander", "Charmeleon", "Charizard"],
    "Water": ["Squirtle", "Bulbasaur", "Ivysaur"],
    "Grass": ["Charmander", "Charmeleon", "Charizard"],
}

print("Fire" in pokemon)
print("Grass" in pokemon)
print("Electric" in pokemon)
print("Electric" not in pokemon)
print("fire" in pokemon)


if "Zombie" in pokemon:
    print(pokemon["Zombie"])
else:
    print("The category Zombie does not exist in the pokemon dictionary.")