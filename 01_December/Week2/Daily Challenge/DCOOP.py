# -------------------------
# Challenge 1: Sorting
# -------------------------
user_input = input("Enter comma-separated words: ").strip()  # e.g. without,hello,bag,world
words = user_input.split(",")
words.sort()  # alphabetical
print(",".join(words))


# -------------------------
# Challenge 2: Longest Word
# -------------------------
def longest_word(sentence: str) -> str:
    words = sentence.split()  # punctuation stays attached, as required
    longest = ""
    for w in words:
        if len(w) > len(longest):
            longest = w
    return longest


# Tests (expected outputs)
print(longest_word("Margaret's toy is a pretty doll."))          # Margaret's
print(longest_word("A thing of beauty is a joy forever."))       # forever.
print(longest_word("Forgetfulness is by all means powerless!"))  # Forgetfulness
