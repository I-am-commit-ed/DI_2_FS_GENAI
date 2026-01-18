import random
from dataclasses import dataclass

@dataclass(frozen=True)
class Card:
    suit: str
    value: str

    def __str__(self) -> str:
        return f"{self.value} of {self.suit}"


class Deck:
    SUITS = ("Hearts", "Diamonds", "Clubs", "Spades")
    VALUES = ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K")

    def __init__(self) -> None:
        self._cards: list[Card] = []
        self.shuffle()  # start with a full shuffled deck

    def shuffle(self) -> None:
        """
        Ensure the deck has all 52 cards (fresh full deck), then shuffle randomly.
        """
        self._cards = [Card(suit, value) for suit in self.SUITS for value in self.VALUES]
        random.shuffle(self._cards)

    def deal(self) -> Card:
        """
        Deal (remove and return) one card from the deck.
        """
        if not self._cards:
            raise IndexError("Cannot deal from an empty deck.")
        return self._cards.pop()

    def __len__(self) -> int:
        return len(self._cards)
