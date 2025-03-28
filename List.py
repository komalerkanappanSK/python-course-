# Creating a list
fruits = ["apple", "banana", "cherry", "apple"]

# Access elements
print(fruits[0])  # Output: apple
print(fruits[-1])  # Output: apple (negative index)

# Modify elements
fruits[1] = "blueberry"  
print(fruits)  # Output: ['apple', 'blueberry', 'cherry', 'apple']

# Add elements
fruits.append("orange")  # Add at the end
fruits.insert(1, "grape")  # Insert at index 1
print(fruits)  

# Remove elements
fruits.remove("apple")  # Removes first occurrence
popped_item = fruits.pop()  # Removes last item
del fruits[0]  # Delete by index

# List Comprehension
squared = [x**2 for x in range(5)]  # Output: [0, 1, 4, 9, 16]
