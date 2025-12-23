# 🌟 Birthday Cake Program
# Key Python Topics:
# input()
# Strings
# Integers
# Conditionals
# Basic date logic


# Ask the user for their birthdate (DD/MM/YYYY)
birthdate = input("Enter your birthdate (DD/MM/YYYY): ")

day, month, year = birthdate.split("/")
year = int(year)

# Current year (simple approach, no imports)
current_year = 2025

# Calculate age
age = current_year - year

# Number of candles = last digit of age
candles = age % 10
candle_str = "i" * candles

# Check leap year
is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def print_cake():
    print(f"       ___{candle_str}___")
    print("      |:H:a:p:p:y:|")
    print("    __|___________|__")
    print("   |^^^^^^^^^^^^^^^^^|")
    print("   |:B:i:r:t:h:d:a:y:|")
    print("   |                 |")
    print("   ~~~~~~~~~~~~~~~~~~~")


# Display cake(s)
print_cake()

if is_leap:
    print()
    print_cake()
