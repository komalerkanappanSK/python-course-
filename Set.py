# Creating a set
numbers = {1, 2, 3, 4, 2, 3}  # Duplicates are removed automatically
print(numbers)  # Output: {1, 2, 3, 4}

# Add elements
numbers.add(5)

# Remove elements
numbers.remove(3)  # Removes element (Error if not found)
numbers.discard(10)  # Removes without error if not found

# Set Operations
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print(A | B)  # Union → {1, 2, 3, 4, 5, 6}
print(A & B)  # Intersection → {3, 4}
print(A - B)  # Difference → {1, 2}
print(A ^ B)  # Symmetric Difference → {1, 2, 5, 6}
