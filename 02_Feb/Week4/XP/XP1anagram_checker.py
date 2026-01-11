# =========================
# anagram_checker.py
# =========================
from __future__ import annotations
from pathlib import Path
from typing import List, Set


class AnagramChecker:
    """
    Logic-only class (NO printing).
    Loads a word list once, checks validity, and finds anagrams.
    """

    def __init__(self, word_list_path: str = "wordlist.txt"):
        path = Path(word_list_path)
        if not path.exists():
            raise FileNotFoundError(f"Word list file not found: {path.resolve()}")

        # Store as uppercase words for fast, case-insensitive matching
        with path.open("r", encoding="utf-8") as f:
            words = [line.strip() for line in f if line.strip()]

        self.words: Set[str] = {w.upper() for w in words if w.isalpha()}

    def is_valid_word(self, word: str) -> bool:
        """
        Returns True if `word` exists in the word list (case-insensitive).
        """
        if not isinstance(word, str):
            return False
        clean = word.strip()
        if not clean or not clean.isalpha():
            return False
        return clean.upper() in self.words

    @staticmethod
    def is_anagram(word1: str, word2: str) -> bool:
        """
        Returns True if word1 and word2 are anagrams of each other, False otherwise.
        Not an anagram if they are the exact same word.
        """
        if not (isinstance(word1, str) and isinstance(word2, str)):
            return False

        w1 = word1.strip().upper()
        w2 = word2.strip().upper()

        if not (w1.isalpha() and w2.isalpha()):
            return False

        if w1 == w2:
            return False

        return sorted(w1) == sorted(w2)

    def get_anagrams(self, word: str) -> List[str]:
        """
        Returns a list of anagrams (lowercase) for the given word, excluding the word itself.
        If the word is not valid, returns an empty list.
        """
        if not self.is_valid_word(word):
            return []

        target = word.strip().upper()
        target_sorted = sorted(target)
        target_len = len(target)

        results = []
        for w in self.words:
            if len(w) != target_len:
                continue
            if w == target:
                continue
            if sorted(w) == target_sorted:
                results.append(w.lower())

        # stable output
        results.sort()
        return results