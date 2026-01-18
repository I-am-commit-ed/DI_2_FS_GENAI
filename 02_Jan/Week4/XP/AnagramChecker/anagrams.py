"""anagrams.py

Command-line UI for the anagram checker.

Run:
    python anagrams.py

It relies on anagram_checker.AnagramChecker for the logic.
"""

from __future__ import annotations

from pathlib import Path

from anagram_checker import AnagramChecker


def _normalize_user_word(raw: str) -> str | None:
    """Validate and normalize user input.

    Rules:
    - Must be exactly one word.
    - Must contain only alphabetic characters.
    - Leading/trailing whitespace is ignored.

    Returns:
        Normalized word (lowercase) if valid, otherwise None.
    """
    if raw is None:
        return None

    cleaned = raw.strip()
    if not cleaned:
        return None

    parts = cleaned.split()
    if len(parts) != 1:
        return None

    word = parts[0]
    if not word.isalpha():
        return None

    return word.lower()


def _print_word_result(checker: AnagramChecker, word: str) -> None:
    """Print a formatted result for the given word."""
    print(f'\nYOUR WORD : "{word.upper()}"')

    if checker.is_valid_word(word):
        print("This is a valid English word.")
        anagrams = checker.get_anagrams(word)
        if anagrams:
            print("Anagrams for your word:", ", ".join(anagrams))
        else:
            print("Anagrams for your word: (none found)")
    else:
        print("This is NOT a valid English word in the word list.")


def main() -> None:
    # Default to a word list in the same folder as this script.
    # If you put your word list elsewhere, change this path.
    default_word_list = Path(__file__).with_name("sowpods.txt")

    try:
        checker = AnagramChecker(default_word_list)
    except FileNotFoundError:
        # Fall back to common workshop path if the file was extracted there.
        # (No printing inside AnagramChecker; UI handles messaging.)
        fallback = Path("/mnt/data/sowpods.txt")
        checker = AnagramChecker(fallback)

    while True:
        print("\n--- ANAGRAM CHECKER ---")
        print("1) Enter a word")
        print("2) Exit")

        choice = input("Choose an option (1/2): ").strip()

        if choice == "2":
            print("Goodbye!")
            break

        if choice != "1":
            print("Invalid choice. Please type 1 or 2.")
            continue

        user_input = input("Enter a word: ")
        word = _normalize_user_word(user_input)

        if word is None:
            print(
                "Error: Please enter ONE word using only letters (A-Z). "
                "No numbers, spaces, or special characters."
            )
            continue

        _print_word_result(checker, word)


if __name__ == "__main__":
    main()
