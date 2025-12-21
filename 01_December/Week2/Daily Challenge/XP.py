# ======================================
# Exercise 1: Hello World
# ======================================

print("Hello world\n" * 4)


# ======================================
# Exercise 2: Some Math
# ======================================

result = (99 ** 3) * 8
print(result)


# ======================================
# Exercise 3: What is the output?
# ======================================

# My guesses are written as comments
print(15 < 8)        # False
print(5 < 3)         # False
print(3 == 3)        # True
print(3 == "3")      # False

# The next line would cause a TypeError in Python 3, so it's commented out
# print("3" > 3)

print("Hello" == "hello")  # False


# ======================================
# 🌟 Exercise 4: Your computer brand
# ======================================

computer_brand = "Apple"
print(f"I have a {computer_brand} computer.")


# ======================================
# 🌟 Exercise 5: Your information
# ======================================

name = "Manuel"
age = 30
shoe_size = 43

info = f"My name is {name}, I am {age} years old, and my shoe size is {shoe_size}."
print(info)


# ======================================
# 🌟 Exercise 6: A & B
# ======================================

a = 10
b = 5

if a > b:
    print("Hello World")


# ======================================
# Exercise 7: Odd or Even
# ======================================

number = int(input("Enter a number: "))

if number % 2 == 0:
    print("This number is even.")
else:
    print("This number is odd.")


# ======================================
# Exercise 8: What’s your name?
# ======================================

my_name = "Manuel"
user_name = input("What is your name? ")

if user_name == my_name:
    print("Wow! We have the same name 😄")
else:
    print("Nice to meet you! At least one of us has a cooler name 😉")


# ======================================
# 🌟 Exercise 9: Tall enough to ride a roller coaster
# ======================================

height = int(input("Enter your height in cm: "))

if height > 145:
    print("You are tall enough to ride the roller coaster 🎢")
else:
    print("Sorry, you need to grow some more to ride 😅")
