#                     List comprehension = A concise way to create lists in Python
#                     Compact and easier to read than traditional loops
#                     [expression for value in iterable if condition]


# doubles = [x * 2 for x in range(1,11)]
# thriples = [y * 3 for y in range(1,11)]
# squares = [z * z for z in range(1,11)]

# print(squares)


fruits = ['apple' , 'orange' , 'avacado' , 'cherry']
# upper_case = [fruit.capitalize() for fruit in fruits]
fruit_chars = [fruit[0] for fruit in fruits]

print(fruit_chars)