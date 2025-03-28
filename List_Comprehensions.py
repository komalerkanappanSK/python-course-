#List comprehensions provide a concise way to create lists in Python.
#they consist of brackets containing an expression followed by a for clause,
#then zero or more for or if clauses.
#List comprehensions are generally more readable and often more efficient than equivalent for loops,
#especially for simple transformations and filtering operations.

#Basic Syntax
#[expression for item in iterable]
# Simple list comprehension
squares = [x**2 for x in range(10)]
print(f" Simple list comprehension : {squares}")
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]


#With conditional
even_squares = [x**2 for x in range(10) if x % 2 == 0]
print(f" With conditional : {even_squares}")
# [0, 4, 16, 36, 64]


#Nested loops
pairs = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
print(f" Nested loops : {pairs}")
# [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]

# Flattening a matrix
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for row in matrix for num in row]
print(f" Flattening a matrix: {flattened}")
# [1, 2, 3, 4, 5, 6, 7, 8, 9]

#Conditional expression
results = ["Even" if x % 2 == 0 else "Odd" for x in range(5)]
print(f" Conditional expression : {results}")
# ['Even', 'Odd', 'Even', 'Odd', 'Even']

#Dictionary comprehension
square_dict = {x: x**2 for x in range(5)}
print(f" Dictionary comprehension  : {square_dict}")
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
