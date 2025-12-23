# OOP Exercises 1–4 (Cats, Dogs, Song, Zoo) - copy/paste once

# -----------------------------
# 🌟 Exercise 1: Cats
# -----------------------------
class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age


# Step 1: Create cat objects
cat1 = Cat("Milo", 4)
cat2 = Cat("Luna", 7)
cat3 = Cat("Simba", 5)


# Step 2: Function to find the oldest cat
def find_oldest_cat(cat1, cat2, cat3):
    oldest = cat1
    if cat2.age > oldest.age:
        oldest = cat2
    if cat3.age > oldest.age:
        oldest = cat3
    return oldest


# Step 3: Print the oldest cat's details
oldest_cat = find_oldest_cat(cat1, cat2, cat3)
print(f"The oldest cat is {oldest_cat.name}, and is {oldest_cat.age} years old.")

print("\n" + "-" * 50 + "\n")

# -----------------------------
# 🌟 Exercise 2: Dogs
# -----------------------------
class Dog:
    def __init__(self, name, height):
        self.name = name
        self.height = height  # in cm

    def bark(self):
        print(f"{self.name} goes woof!")

    def jump(self):
        print(f"{self.name} jumps {self.height * 2} cm high!")


# Step 2: Create Dog objects
davids_dog = Dog("Rex", 50)
sarahs_dog = Dog("Teacup", 20)

# Step 3: Print details and call methods
print(f"David's dog: {davids_dog.name}, height: {davids_dog.height} cm")
davids_dog.bark()
davids_dog.jump()

print()

print(f"Sarah's dog: {sarahs_dog.name}, height: {sarahs_dog.height} cm")
sarahs_dog.bark()
sarahs_dog.jump()

print()

# Step 4: Compare sizes
if davids_dog.height > sarahs_dog.height:
    print(f"{davids_dog.name} is taller than {sarahs_dog.name}.")
elif sarahs_dog.height > davids_dog.height:
    print(f"{sarahs_dog.name} is taller than {davids_dog.name}.")
else:
    print(f"{davids_dog.name} and {sarahs_dog.name} are the same height.")

print("\n" + "-" * 50 + "\n")

# -----------------------------
# 🌟 Exercise 3: Who’s the song producer?
# -----------------------------
class Song:
    def __init__(self, lyrics):
        self.lyrics = lyrics  # list of strings

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)


stairway = Song([
    "There’s a lady who's sure",
    "all that glitters is gold",
    "and she’s buying a stairway to heaven"
])

stairway.sing_me_a_song()

print("\n" + "-" * 50 + "\n")

# -----------------------------
# 🌟 Exercise 4: Afternoon at the Zoo
# -----------------------------
class Zoo:
    def __init__(self, zoo_name):
        self.zoo_name = zoo_name
        self.animals = []
        self.groups = {}

    # Bonus: *args so you can pass many animals at once
    def add_animal(self, *new_animals):
        for animal in new_animals:
            if animal not in self.animals:
                self.animals.append(animal)

    def get_animals(self):
        if not self.animals:
            print("No animals in the zoo yet.")
            return
        print("Animals in the zoo:")
        for animal in self.animals:
            print("-", animal)

    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)

    def sort_animals(self):
        self.animals.sort()
        grouped = {}

        for animal in self.animals:
            first_letter = animal[0].upper()
            if first_letter not in grouped:
                grouped[first_letter] = []
            grouped[first_letter].append(animal)

        self.groups = grouped
        return grouped

    def get_groups(self):
        if not self.groups:
            print("No groups yet. Call sort_animals() first.")
            return

        for letter in self.groups:
            print(f"{letter}: {self.groups[letter]}")


# Step 2: Create a Zoo instance
brooklyn_safari = Zoo("Brooklyn Safari")

# Step 3: Use the Zoo methods
brooklyn_safari.add_animal("Giraffe", "Bear", "Baboon", "Cat", "Cougar", "Lion", "Zebra")
brooklyn_safari.get_animals()

print("\nSelling Bear...\n")
brooklyn_safari.sell_animal("Bear")
brooklyn_safari.get_animals()

print("\nSorting + grouping...\n")
brooklyn_safari.sort_animals()
brooklyn_safari.get_groups()
