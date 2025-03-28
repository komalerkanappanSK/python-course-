fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)


    #range
fruits = ["apple", "banana", "cherry"]

for i in range(len(fruits)):
    print(f"Index {i}: {fruits[i]}")

#enumerate
fruits = ["apple", "banana", "cherry"]

for i, fruit in enumerate(fruits):
    print(f"Index {i}: {fruit}")

#reverse
fruits = ["apple", "banana", "cherry"]

for fruit in reversed(fruits):
    print(fruit)

#sorted-sort
fruits = ["apple", "banana", "cherry"]

for fruit in sorted(fruits):
    print(fruit)

#uppercase
fruits = ["apple", "banana", "cherry"]
uppercase_fruits = [fruit.upper() for fruit in fruits]

print(uppercase_fruits)

