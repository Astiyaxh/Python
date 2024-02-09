def fancy_cleanup(string):
    return string.strip().replace("g", "z").replace(" ", "!")

print(fancy_cleanup("       geronimo crikey  "))
print(fancy_cleanup("       nonsense  "))
print(fancy_cleanup("grade"))