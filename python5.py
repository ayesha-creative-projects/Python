# lists
fruits = ["apple", "orange", "banana", "coconut"]
print(len(fruits))

print(f"Apple is in {fruits.index('apple')} index")
print(f"There is only {fruits.count('banana')} banana")

fruits[0] = "pineapple"
fruits.append("pineapple")
fruits.remove("pineapple")
fruits.insert(1, "kiwi")
fruits.sort()
fruits.reverse()


for fruit in fruits:
    print(fruit)

# set
fruits_set = {"apple", "orange", "banana", "coconut"}
fruits_set.add("pineapple")
fruits_set.remove("apple")
fruits_set.pop()  # removes a random item
print(fruits_set)

# tuple
fruits_tuple = ("apple", "orange", "banana", "coconut")
print(len(fruits_tuple))
print(fruits_tuple.index("apple"))
print(fruits_tuple.count("coconut"))

# 2D list
fruits = ["apple", "orange", "banana", "coconut"]
vegetables = ["carrots", "onion", "potatoes"]
meats = ["chicken", "fish", "goat"]

groceries = [fruits, vegetables, meats]
print(groceries)
print(groceries[0])
print(groceries[0][1])

for collection in groceries:
    for item in collection:
        print(item, end=" ")
    print()

# 2D keypad
num_pad = ((1, 2, 3),
           (4, 5, 6),
           (7, 8, 9),
           ("*", 0, "#"))

for row in num_pad:
    for num in row:
        print(num, end=" ")
    print()
