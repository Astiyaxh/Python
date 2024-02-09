job_opening = ("Software Enginner", "New York City", 100000)
position, city, salary = job_opening
print(position, city, salary)

address = ("35 Elm Street", "San Fransisco", "CA", "94107")
street, *city_and_state, zip_code = address 
print(street)
print(city_and_state)
print(zip_code)

# def sum_of_evens_and_odds(elements):
#     evens = 0
#     odds = 0
#     for element in elements:
#         if element % 2 == 0:
#             evens += element
#         else:
#             odds += element
#     return f"({evens}, {odds})"

def sum_of_evens_and_odds(number):
    even_numbers = [num for num in number if num % 2 == 0]
    odd_numbers = [num for num in number if num % 2 != 0]

    return (sum(even_numbers), sum(odd_numbers))


print(sum_of_evens_and_odds((1, 2, 3, 4)))



