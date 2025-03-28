#list
my_list = [1, 2, 3, 4, 2]  # Duplicates allowed
my_list.append(5)          # Add item
my_list[0] = 100           # Modify item
print(my_list)  # Output: [100, 2, 3, 4, 2, 5]

#tuple
my_tuple = (1, 2, 3, 4)  # Immutable
print(my_tuple)

#set
my_set = {1, 2, 3, 4}  # Unique items
my_set.add(5)           # Add item
my_set.remove(3)        # Remove item
print(my_set)
# Output: {1, 2, 4, 5} (Order may vary)

#dictionary

my_dict = {"name": "John", "age": 30, "city": "New York"}
print(my_dict)
my_dict["age"] = 26  # Modify value
my_dict["gender"] = "Female"  # Add new key-value pair
print(my_dict)  
# Output: {'name': 'John', 'age': 26, 'city': 'New York', 'gender': 'Male'}


