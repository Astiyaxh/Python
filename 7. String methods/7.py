empty_space = "          content                "

print(len(empty_space))

print(empty_space.rstrip())
print(len(empty_space.rstrip()))

print(empty_space.lstrip())
print(len(empty_space.lstrip()))

print(empty_space.strip())
print(len(empty_space.strip()))

website = "www.python.org"
print(website.lstrip("w"))
print(website.rstrip(".org"))
print(website.strip("worg."))
print(website.strip("w"))
print(website.strip(""))
