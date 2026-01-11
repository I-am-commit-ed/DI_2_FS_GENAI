"""
Text + TextModification — COPY/PASTE READY

Implements:
- Text: analyze text from a string or file
  - word_frequency(word)
  - most_common_word()
  - unique_words()
  - from_file(file_path)  [class method]

- TextModification(Text): clean text
  - remove_punctuation()
  - remove_stop_words()
  - remove_special_characters()

Notes:
- Cleaning methods update self.text AND also return the modified text.
- Word analysis is case-insensitive by default.
"""

from __future__ import annotations
from dataclasses import dataclass
from pathlib import Path
from typing import Optional, List
import re
import string
from collections import Counter


# A reasonable built-in English stop words set (you can expand it if needed).
STOP_WORDS = {
    "a", "an", "and", "are", "as", "at", "be", "because", "been", "before", "being",
    "but", "by", "can", "could", "did", "do", "does", "doing", "down", "during",
    "each", "few", "for", "from", "further", "had", "has", "have", "having", "he",
    "her", "here", "hers", "herself", "him", "himself", "his", "how", "i", "if",
    "in", "into", "is", "it", "its", "itself", "just", "me", "more", "most", "my",
    "myself", "no", "nor", "not", "now", "of", "off", "on", "once", "only", "or",
    "other", "our", "ours", "ourselves", "out", "over", "own", "same", "she",
    "should", "so", "some", "such", "than", "that", "the", "their", "theirs",
    "them", "themselves", "then", "there", "these", "they", "this", "those",
    "through", "to", "too", "under", "until", "up", "very", "was", "we", "were",
    "what", "when", "where", "which", "while", "who", "whom", "why", "will",
    "with", "you", "your", "yours", "yourself", "yourselves"
}


@dataclass
class Text:
    text: str

    def _tokens(self) -> List[str]:
        """
        Tokenizes the text into words (letters/numbers/underscore) and lowercases them.
        This makes analysis more consistent than naive split().
        """
        return re.findall(r"\b\w+\b", self.text.lower())

    def word_frequency(self, word: str) -> Optional[int]:
        """
        Count occurrences of `word` in the text (case-insensitive).
        Returns None if word is not found.
        """
        if not isinstance(word, str) or not word.strip():
            raise ValueError("word must be a non-empty string")

        tokens = self._tokens()
        target = word.lower()
        count = tokens.count(target)

        return count if count > 0 else None

    def most_common_word(self) -> Optional[str]:
        """
        Returns the most common word in the text (case-insensitive).
        Returns None if there are no words.
        """
        tokens = self._tokens()
        if not tokens:
            return None

        counts = Counter(tokens)
        return counts.most_common(1)[0][0]

    def unique_words(self) -> List[str]:
        """
        Returns unique words as a list (case-insensitive), sorted for stable output.
        """
        tokens = self._tokens()
        return sorted(set(tokens))

    @classmethod
    def from_file(cls, file_path: str) -> "Text":
        """
        Reads a file and returns a Text instance containing its content.
        """
        path = Path(file_path)
        try:
            content = path.read_text(encoding="utf-8")
        except FileNotFoundError:
            raise FileNotFoundError(f"File not found: {path.resolve()}")
        except OSError as e:
            raise OSError(f"Could not read file '{path.resolve()}': {e}")

        return cls(content)


class TextModification(Text):
    def remove_punctuation(self) -> str:
        """
        Removes punctuation characters from the text using string.punctuation.
        Updates self.text and returns it.
        """
        translator = str.maketrans("", "", string.punctuation)
        self.text = self.text.translate(translator)
        return self.text

    def remove_stop_words(self) -> str:
        """
        Removes common English stop words.
        Updates self.text and returns it.
        """
        words = self._tokens()  # lowercased tokens (no punctuation-heavy tokens)
        filtered = [w for w in words if w not in STOP_WORDS]
        self.text = " ".join(filtered)
        return self.text

    def remove_special_characters(self) -> str:
        """
        Removes special characters using regex.
        Keeps letters, numbers, spaces. Collapses multiple spaces.
        Updates self.text and returns it.
        """
        # Replace anything that's not alphanumeric or whitespace with a space
        cleaned = re.sub(r"[^A-Za-z0-9\s]+", " ", self.text)
        # Collapse multiple whitespace
        cleaned = re.sub(r"\s+", " ", cleaned).strip()
        self.text = cleaned
        return self.text


# -------------------------
# Demo / quick tests
# -------------------------
if __name__ == "__main__":
    sample = "Hello, hello!! This is a test. A test, indeed; a SIMPLE test."

    t = Text(sample)
    print("Most common:", t.most_common_word())          # "test" or "hello" depending on counts
    print("Frequency('test'):", t.word_frequency("test"))# 3
    print("Unique words:", t.unique_words())

    tm = TextModification(sample)
    print("\nOriginal:", tm.text)
    print("No punctuation:", tm.remove_punctuation())
    # Reset text for next demo
    tm.text = sample
    print("No special chars:", tm.remove_special_characters())
    tm.text = sample
    print("No stop words:", tm.remove_stop_words())

    # File example (uncomment and set a real path):
    # tf = Text.from_file("my_text_file.txt")
    # print(tf.most_common_word())
