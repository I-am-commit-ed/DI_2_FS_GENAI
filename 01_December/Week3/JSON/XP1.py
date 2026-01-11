# DC1.py — Exercises 1 + 2 (copy/paste)

import json
import random
from pathlib import Path


# =========================================================
# 🌟 Exercise 1: Random Sentence Generator
# =========================================================

WORDS_FILE = "sowpods.txt"  # change this if your word list file has a different name


def get_words_from_file(file_path: str) -> list[str]:
    """
    Reads a word list file and returns a list of words.
    """
    path = Path(file_path)

    # File handling + error handling
    try:
        with path.open("r", encoding="utf-8") as f:
            content = f.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"Word list file not found: {path.resolve()}")
    except OSError as e:
        raise OSError(f"Could not read file '{path.resolve()}': {e}")

    # String manipulation
    words = content.split()
    return words


def get_random_sentence(sentence_length: int, file_path: str = WORDS_FILE) -> str:
    """
    Generates a random sentence (lowercase) with `sentence_length` words.
    """
    words = get_words_from_file(file_path)
    if not words:
        raise ValueError("Word list is empty. Add words to the file and try again.")

    # Random selection
    chosen = [random.choice(words) for _ in range(sentence_length)]
    sentence = " ".join(chosen).lower()
    return sentence


def main() -> None:
    """
    Handles user input, validates it, and prints a random sentence.
    """
    print("Random Sentence Generator")
    print("This program generates a random sentence from a word list.")
    print(f"Word list file: {Path(WORDS_FILE).resolve()}")

    user_input = input("Enter sentence length (2–20): ").strip()

    # Input validation + error handling
    try:
        length = int(user_input)
    except ValueError:
        print("Error: Please enter a valid integer.")
        return

    if length < 2 or length > 20:
        print("Error: Sentence length must be between 2 and 20 (inclusive).")
        return

    try:
        sentence = get_random_sentence(length, WORDS_FILE)
    except Exception as e:
        print(f"Error: {e}")
        return

    print("\nGenerated sentence:")
    print(sentence)


# =========================================================
# 🌟 Exercise 2: Working with JSON
# =========================================================

sampleJson = """{
   "company":{
      "employee":{
         "name":"emma",
         "payable":{
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""


def json_exercise_save_modified(birth_date: str = "1999-12-31", out_file: str = "modified_employee.json") -> None:
    """
    Loads JSON, prints nested salary, adds birth_date to employee, saves to file.
    """
    # Step 1: Load JSON string
    data = json.loads(sampleJson)

    # Step 2: Access nested salary
    salary = data["company"]["employee"]["payable"]["salary"]
    print("\nJSON Exercise")
    print("Salary:", salary)

    # Step 3: Add birth_date
    data["company"]["employee"]["birth_date"] = birth_date

    # Step 4: Save modified JSON to file
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

    print(f"Modified JSON saved to: {Path(out_file).resolve()}")


# =========================================================
# Run
# =========================================================

if __name__ == "__main__":
    # Exercise 1
    main()

    # Exercise 2
    json_exercise_save_modified(birth_date="2001-09-07", out_file="modified_employee.json")
