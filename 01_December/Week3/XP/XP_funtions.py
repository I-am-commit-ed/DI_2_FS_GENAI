import random

# ======================================
# 🌟 Exercise 1: What Are You Learning?
# ======================================

def display_message():
    print("I am learning about functions in Python.")

display_message()
print()


# ======================================
# 🌟 Exercise 2: What’s Your Favorite Book?
# ======================================

def favorite_book(title):
    print(f"One of my favorite books is {title}.")

favorite_book("Alice in Wonderland")
print()


# ======================================
# 🌟 Exercise 3: Some Geography
# ======================================

def describe_city(city, country="Unknown"):
    print(f"{city} is in {country}.")

describe_city("Reykjavik", "Iceland")
describe_city("Paris")
print()


# ======================================
# 🌟 Exercise 4: Random
# ======================================

def compare_numbers(user_number):
    random_number = random.randint(1, 100)

    if user_number == random_number:
        print("Success! The numbers match.")
    else:
        print(f"Fail! Your number: {user_number}, Random number: {random_number}")

compare_numbers(50)
print()


# ======================================
# 🌟 Exercise 5: Let’s Create Some Personalized Shirts!
# ======================================

def make_shirt(size="large", text="I love Python"):
    print(f"The size of the shirt is {size} and the text is {text}.")

# Default values
make_shirt()

# Medium size, default text
make_shirt(size="medium")

# Custom size and message
make_shirt(size="small", text="Custom message")

# Bonus: Keyword arguments
make_shirt(text="Hello!", size="small")
print()


# ======================================
# 🌟 Exercise 6: Magicians…
# ======================================

magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']

def show_magicians(names):
    for name in names:
        print(name)

def make_great(names):
    for i in range(len(names)):
        names[i] = f"{names[i]} the Great"

make_great(magician_names)
show_magicians(magician_names)
print()


# ======================================
# 🌟 Exercise 7: Temperature Advice
# ======================================

def get_random_temp():
    return random.uniform(-10, 40)

def main():
    temperature = round(get_random_temp(), 1)
    print(f"The temperature right now is {temperature} degrees Celsius.")

    if temperature < 0:
        print("Brrr, that’s freezing! Wear some extra layers today.")
    elif 0 <= temperature <= 16:
        print("Quite chilly! Don’t forget your coat.")
    elif 16 < temperature <= 23:
        print("Nice weather.")
    elif 24 <= temperature <= 32:
        print("A bit warm, stay hydrated.")
    else:
        print("It’s really hot! Stay cool.")

main()
