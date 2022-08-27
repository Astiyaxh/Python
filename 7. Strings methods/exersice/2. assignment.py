# Define a fancy_cleanup fucntion that accepts a single string argument
# The function should clean up the whitespace on both side of the
# argument. It should also replace every occurence of the letter "g" with the
# letter "z" and every occurence of a space with an exclamation point (!).
#
# fancy_cleanup("          geronimo crikey  ")  => "zeronimo!crikey"
# fancy_cleanup("             nonsense  ")      => "nonsense"
# fancy_cleanup("grade")                        => "zrade"       


def fancy_cleanup(text):
    return (text.strip().replace("g","z").replace(" ","!"))

print(fancy_cleanup("          geronimo crikey  "))