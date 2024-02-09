def nested_sum(lists):
    total = 0
    for row in lists:
        for value in row:
            total += value

    return total

print(nested_sum([[1, 2, 3],[4, 5]]))
print(nested_sum([[1, 2, 3], [], [], [4], [5]]))
print(nested_sum([[]]))

def fancy_concatenate(lists):
    final = ""
    for row in lists:
        if len(row) == 3:
            for string in row:
                final += string
    
    return final

print(fancy_concatenate([["A", "B", "C"]]))
print(fancy_concatenate([["A", "B", "C"], ["D", "E", "F"]]))
print(fancy_concatenate([["A", "B", "C"], ["D", "E", "F", "G"]]))
print(fancy_concatenate([["A", "B", "C"], ["D", "E"]]))
print(fancy_concatenate([["A", "B"], ["C", "D"]]))