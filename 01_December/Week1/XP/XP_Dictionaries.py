# ======================================
# 🌟 Exercise 1: Converting Lists into Dictionaries
# ======================================

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

result_dict = dict(zip(keys, values))
print("Exercise 1 Output:")
print(result_dict)
print()


# ======================================
# 🌟 Exercise 2: Cinemax #2
# ======================================

family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}

total_cost = 0

print("Exercise 2 Output:")
for name, age in family.items():
    if age < 3:
        price = 0
    elif 3 <= age <= 12:
        price = 10
    else:
        price = 15

    total_cost += price
    print(f"{name.title()} pays ${price}")

print(f"Total cost: ${total_cost}")
print()

# Bonus: User input version
print("Exercise 2 Bonus:")
user_family = {}
while True:
    name = input("Enter family member name (or 'done' to finish): ")
    if name.lower() == "done":
        break
    age = int(input(f"Enter {name}'s age: "))
    user_family[name] = age

bonus_total = 0
for name, age in user_family.items():
    if age < 3:
        price = 0
    elif 3 <= age <= 12:
        price = 10
    else:
        price = 15
    bonus_total += price

print(f"Total ticket cost: ${bonus_total}")
print()


# ======================================
# 🌟 Exercise 3: Zara
# ======================================

brand = {
    "name": "Zara",
    "creation_date": 1975,
    "creator_name": "Amancio Ortega Gaona",
    "type_of_clothes": ["men", "women", "children", "home"],
    "international_competitors": ["Gap", "H&M", "Benetton"],
    "number_stores": 7000,
    "major_color": {
        "France": "blue",
        "Spain": "red",
        "US": ["pink", "green"]
    }
}

# Modify number_stores
brand["number_stores"] = 2

# Print client description
print("Exercise 3 Output:")
print(f"Zara clients include: {', '.join(brand['type_of_clothes'])}")

# Add country_creation
brand["country_creation"] = "Spain"

# Add Desigual if competitors exist
if "international_competitors" in brand:
    brand["international_competitors"].append("Desigual")

# Delete creation_date
brand.pop("creation_date")

# Print last competitor
print("Last international competitor:", brand["international_competitors"][-1])

# Print US colors
print("Major colors in the US:", brand["major_color"]["US"])

# Print number of keys
print("Number of keys in brand dictionary:", len(brand))

# Print all keys
print("Brand keys:", list(brand.keys()))
print()

# Bonus: Merge dictionaries
more_on_zara = {
    "creation_date": 1975,
    "number_stores": 2
}

brand.update(more_on_zara)
print("Merged brand dictionary:")
print(brand)
print()


# ======================================
# 🌟 Exercise 4: Disney Characters
# ======================================

users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]

# 1. Characters to indices
char_to_index = {name: index for index, name in enumerate(users)}

# 2. Indices to characters
index_to_char = {index: name for index, name in enumerate(users)}

# 3. Alphabetically sorted characters to indices
sorted_characters = sorted(users)
sorted_char_to_index = {name: index for index, name in enumerate(sorted_characters)}

print("Exercise 4 Output:")
print("Characters to indices:")
print(char_to_index)

print("\nIndices to characters:")
print(index_to_char)

print("\nAlphabetically sorted characters to indices:")
print(sorted_char_to_index)
