import random
from dataclasses import dataclass
from typing import List


@dataclass(frozen=True)
class Card:
    suit: str   # Hearts, Diamonds, Clubs, Spades
    value: str  # A,2,3,4,5,6,7,8,9,10,J,Q,K

    def __str__(self) -> str:
        return f"{self.value} of {self.suit}"


class Deck:
    SUITS = ("Hearts", "Diamonds", "Clubs", "Spades")
    VALUES = ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K")

    def __init__(self):
        # Start with a full deck
        self.cards: List[Card] = [Card(suit, value) for suit in self.SUITS for value in self.VALUES]

    def shuffle(self) -> None:
        """
        Ensure the deck has all 52 cards, then shuffle randomly.
        """
        full_deck = [Card(suit, value) for suit in self.SUITS for value in self.VALUES]

        # If deck is missing cards or has extra/duplicates, reset it
        if len(self.cards) != 52 or set(self.cards) != set(full_deck):
            self.cards = full_deck

        random.shuffle(self.cards)

    def deal(self) -> Card:
        """
        Deal one card from the top of the deck (end of list).
        Removes the card from the deck.
        """
        if not self.cards:
            raise IndexError("Cannot deal from an empty deck.")
        return self.cards.pop()

    def __len__(self) -> int:
        return len(self.cards)


# -------------------------
# Quick test
# -------------------------
if __name__ == "__main__":
    deck = Deck()
    print("Initial deck size:", len(deck))  # 52

    deck.shuffle()
    print("Deck size after shuffle:", len(deck))  # 52

    card = deck.deal()
    print("Dealt:", card)
    print("Deck size after deal:", len(deck))  # 51
