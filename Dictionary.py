# Creating a dictionary
student = {
    "name": "Alice",
    "age": 22,
    "grade": "A"
}

# Access values
print(student["name"])  # Output: Alice
print(student.get("age"))  # Output: 22

# Add/Modify values
student["city"] = "New York"  # Add new key-value pair
student["age"] = 23  # Modify existing value

# Remove key-value pairs
del student["grade"]  # Deletes a key
age = student.pop("age")  # Removes key and returns value

# Iterate over dictionary
for key, value in student.items():
    print(f"{key}: {value}")

# Dictionary Comprehension
squares = {x: x**2 for x in range(5)}  
print(squares)  # Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
