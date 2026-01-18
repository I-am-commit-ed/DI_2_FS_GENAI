"""
anagram_checker.py

Contains the AnagramChecker class.

Notes:
- No printing should happen inside this module.
- Words are handled case-insensitively.
"""

from __future__ import annotations

from pathlib import Path
from typing import List, Set


class AnagramChecker:
    """Load a word list and provide anagram-related utilities."""

    def __init__(self, word_list_path: str | Path = "sowpods.txt") -> None:
        """
        Load the word list file into memory.

        Args:
            word_list_path: Path to a newline-separated word list.
        """
        path = Path(word_list_path)
        if not path.exists():
            raise FileNotFoundError(f"Word list file not found: {path.resolve()}")

        # Store words in lowercase for case-insensitive checks.
        # A set gives O(1) membership checks.
        self._words: Set[str] = set()
        with path.open("r", encoding="utf-8", errors="ignore") as f:
            for line in f:
                w = line.strip().lower()
                if w:
                    self._words.add(w)

    def is_valid_word(self, word: str) -> bool:
        """Return True if the given word exists in the loaded word list."""
        if not isinstance(word, str):
            return False
        w = word.strip().lower()
        return bool(w) and w in self._words

    @staticmethod
    def is_anagram(word1: str, word2: str) -> bool:
        """Return True if word1 and word2 are anagrams (case-insensitive)."""
        if not isinstance(word1, str) or not isinstance(word2, str):
            return False

        w1 = word1.strip().lower()
        w2 = word2.strip().lower()

        if not w1 or not w2:
            return False
        if len(w1) != len(w2):
            return False

        return sorted(w1) == sorted(w2)

    def get_anagrams(self, word: str) -> List[str]:
        """Return a list of anagrams for the given word (excluding itself)."""
        if not isinstance(word, str):
            return []

        target = word.strip().lower()
        if not target:
            return []

        anagrams: List[str] = []
        for candidate in self._words:
            if candidate == target:
                continue
            if self.is_anagram(target, candidate):
                anagrams.append(candidate)

        anagrams.sort()
        return anagrams
