def length_match(strings, number):
    counter = 0
    for string in strings:
        if len(string) == number:
            counter += 1
    return counter

# print(length_match(["cat", "dog", "kangaroo", "mouse"], 3))
# print(length_match(["cat", "dog", "kangaroo", "mouse"], 5))
# print(length_match(["cat", "dog", "kangaroo", "mouse"], 4))
# print(length_match([], 5))


# def sum_from(start, end):
#     total = 0
#     for number in range(start, end + 1):
#         total += number

#     return total

def sum_from(num1, num2):
    total = 0
    if num1 > num2:
        return f"Num1:{num1} must be smaller than the Num2:{num2}"
    else:
        while num1 <= num2:
            total += num1
            num1 += 1
    return total


# print(sum_from(1,2))
# print(sum_from(1,5))
# print(sum_from(3,8))
# print(sum_from(9,12))
# print(sum_from(19,12))



def same_index_values(list1, list2):
    results = []

    for index, value in enumerate(list1):
        if value == list2[index]:
            results.append(index)
    
    return results

print(same_index_values([1, 2, 3], [3, 2, 1]))
print(same_index_values(['a', 'b', 'c', 'd'], ['c', 'b', 'a', 'd']))