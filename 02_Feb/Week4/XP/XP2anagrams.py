# =========================
# anagrams.py
# =========================
from __future__ import annotations
from anagram_checker import AnagramChecker


def _validate_user_word(raw: str) -> tuple[bool, str]:
    """
    Validates raw user input per requirements:
    - trims whitespace
    - only one word
    - alphabetic only
    Returns: (is_valid, cleaned_word_or_error_message)
    """
    if raw is None:
        return False, "Error: No input provided."

    cleaned = raw.strip()
    if not cleaned:
        return False, "Error: Please type a word."

    parts = cleaned.split()
    if len(parts) != 1:
        return False, "Error: Only a single word is allowed."

    word = parts[0]
    if not word.isalpha():
        return False, "Error: Only alphabetic characters are allowed (A–Z)."

    return True, word


def _print_menu() -> None:
    print("\n--- ANAGRAM CHECKER ---")
    print("1) Input a word")
    print("2) Exit")


def main() -> None:
    checker = None

    while True:
        _print_menu()
        choice = input("Choose an option (1/2): ").strip()

        if choice == "2":
            print("Goodbye.")
            break

        if choice != "1":
            print("Error: Please choose 1 or 2.")
            continue

        user_input = input("Enter a word: ")
        ok, word_or_error = _validate_user_word(user_input)
        if not ok:
            print(word_or_error)
            continue

        word = word_or_error

        # Create the checker instance only when needed (loads file once)
        if checker is None:
            try:
                checker = AnagramChecker("wordlist.txt")
            except FileNotFoundError as e:
                print(f"Error: {e}")
                print("Make sure 'wordlist.txt' is in the same folder as these files.")
                continue

        valid = checker.is_valid_word(word)
        anagrams = checker.get_anagrams(word) if valid else []

        # Output formatting requested
        print(f'\nYOUR WORD : "{word.upper()}"')
        if valid:
            print("This is a valid English word.")
            if anagrams:
                print("Anagrams for your word:", ", ".join(anagrams) + ".")
            else:
                print("Anagrams for your word: (none found).")
        else:
            print("This is NOT a valid English word.")


if __name__ == "__main__":
    main()






