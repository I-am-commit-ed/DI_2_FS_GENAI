# 👩‍🏫 👩🏿‍🏫 What You’ll learn
# Sequence
# List
# Set
# Tuple


# 🌟 Exercise 1: Favorite Numbers
# Key Python Topics:
# Sets
# Adding/removing items in a set
# Set concatenation (using union)

my_fav_numbers = {3, 7, 21}
my_fav_numbers.add(42)
my_fav_numbers.add(99)
my_fav_numbers.remove(99)

friend_fav_numbers = {5, 7, 11}

our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)
print("Our favorite numbers:", our_fav_numbers)


# 🌟 Exercise 2: Tuple
# Key Python Topics:
# Tuples (immutability)

numbers = (1, 2, 3)
# numbers.append(4)  # ❌ This will raise an error because tuples are immutable
print("Tuple:", numbers)


# 🌟 Exercise 3: List Manipulation
# Key Python Topics:
# Lists
# List methods: append, remove, insert, count, clear

basket = ["Banana", "Apples", "Oranges", "Blueberries"]

basket.remove("Banana")
basket.remove("Blueberries")
basket.append("Kiwi")
basket.insert(0, "Apples")

print("Apples count:", basket.count("Apples"))

basket.clear()
print("Final basket:", basket)


# 🌟 Exercise 4: Floats
# Key Python Topics:
# Lists
# Floats and integers
# Range generation

# A float is a number with a decimal point (e.g. 1.5)
# An integer is a whole number (e.g. 2)

numbers = []
for i in range(3, 11):
    numbers.append(i / 2)

print("Float and int sequence:", numbers)


# 🌟 Exercise 5: For Loop
# Key Python Topics:
# Loops (for)
# Range and indexing

for i in range(1, 21):
    print(i)

for i in range(1, 21):
    if i % 2 == 0:
        print(i)


# 🌟 Exercise 6: While Loop
# Key Python Topics:
# Loops (while)
# Conditionals

while True:
    name = input("Enter your name: ")

    if name.isdigit() or len(name) < 3:
        print("Invalid name, try again.")
    else:
        print("Thank you")
        break


# 🌟 Exercise 7: Favorite Fruits
# Key Python Topics:
# Input/output
# Strings and lists
# Conditionals

favorite_fruits = input("Enter your favorite fruits (space-separated): ").split()
fruit = input("Enter a fruit name: ")

if fruit in favorite_fruits:
    print("You chose one of your favorite fruits! Enjoy!")
else:
    print("You chose a new fruit. I hope you enjoy it!")


# 🌟 Exercise 8: Pizza Toppings
# Key Python Topics:
# Loops
# Lists
# String formatting

toppings = []
base_price = 10
topping_price = 2.5

while True:
    topping = input("Enter a pizza topping (type 'quit' to stop): ")
    if topping == "quit":
        break
    toppings.append(topping)
    print(f"Adding {topping} to your pizza.")

total_cost = base_price + len(toppings) * topping_price
print("Your toppings:", toppings)
print("Total cost: $", total_cost)


# 🌟 Exercise 9: Cinemax Tickets
# Key Python Topics:
# Conditionals
# Lists
# Loops

total_cost = 0

while True:
    age = input("Enter age (or type 'done' to finish): ")

    if age == "done":
        break

    age = int(age)

    if age < 3:
        cost = 0
    elif 3 <= age <= 12:
        cost = 10
    else:
        cost = 15

    total_cost += cost

print("Total ticket cost: $", total_cost)
