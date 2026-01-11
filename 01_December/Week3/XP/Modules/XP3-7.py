# =========================================================
# 🌟 Exercise 3: String module (random string length 5)
# =========================================================

import random
import string

def random_letters_string(length=5):
    letters = string.ascii_letters  # uppercase + lowercase
    result = ""
    for _ in range(length):
        result += random.choice(letters)
    return result

if __name__ == "__main__":
    print("\n=== Exercise 3 ===")
    print(random_letters_string(5))


# =========================================================
# 🌟 Exercise 4: Current Date
# =========================================================

from datetime import datetime

def show_current_date():
    today = datetime.now().date()
    print(today)

if __name__ == "__main__":
    print("\n=== Exercise 4 ===")
    show_current_date()


# =========================================================
# 🌟 Exercise 5: Time left until January 1st
# =========================================================

from datetime import datetime

def time_until_jan_first():
    now = datetime.now()
    next_year = now.year + 1
    jan_first = datetime(next_year, 1, 1)
    diff = jan_first - now

    days = diff.days
    seconds = diff.seconds
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    secs = seconds % 60

    print(f"Time left until January 1st ({jan_first.date()}): {days} days, {hours} hours, {minutes} minutes, {secs} seconds")

if __name__ == "__main__":
    print("\n=== Exercise 5 ===")
    time_until_jan_first()


# =========================================================
# 🌟 Exercise 6: Birthday and minutes lived
# =========================================================

from datetime import datetime

def minutes_lived(birthdate_str, fmt="%Y-%m-%d"):
    """
    birthdate_str example: "2001-09-07" (default format "%Y-%m-%d")
    """
    birthdate = datetime.strptime(birthdate_str, fmt)
    now = datetime.now()
    diff = now - birthdate
    minutes = int(diff.total_seconds() // 60)
    print(f"You have lived approximately {minutes} minutes.")

if __name__ == "__main__":
    print("\n=== Exercise 6 ===")
    # Example usage:
    # minutes_lived("2000-01-01")
    pass


# =========================================================
# 🌟 Exercise 7: Faker Module (list of dict users)
# =========================================================

def generate_users(n):
    """
    Requires: pip install faker
    """
    from faker import Faker
    fake = Faker()

    users = []
    for _ in range(n):
        user = {
            "name": fake.name(),
            "address": fake.address(),
            "language_code": fake.language_code(),
        }
        users.append(user)
    return users

if __name__ == "__main__":
    print("\n=== Exercise 7 ===")
    # Uncomment after installing faker:
    # users_list = generate_users(3)
    # print(users_list)
    pass