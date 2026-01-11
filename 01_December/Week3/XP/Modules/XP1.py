🌟 Exercise 1: Currencies
# =========================================================

class Currency:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount

    def __str__(self):
        # "1 dollar" vs "5 dollars"
        suffix = "" if self.amount == 1 else "s"
        return f"{self.amount} {self.currency}{suffix}"

    def __repr__(self):
        # Expected: same as __str__ in this exercise
        return str(self)

    def __int__(self):
        return int(self.amount)

    def __add__(self, other):
        # Currency + int
        if isinstance(other, int):
            return self.amount + other

        # Currency + Currency (same currency only)
        if isinstance(other, Currency):
            if self.currency != other.currency:
                raise TypeError(
                    f"Cannot add between Currency type <{self.currency}> and <{other.currency}>"
                )
            return self.amount + other.amount

        return NotImplemented

    def __iadd__(self, other):
        # In-place add: update self.amount, then return self
        if isinstance(other, int):
            self.amount += other
            return self

        if isinstance(other, Currency):
            if self.currency != other.currency:
                raise TypeError(
                    f"Cannot add between Currency type <{self.currency}> and <{other.currency}>"
                )
            self.amount += other.amount
            return self

        raise TypeError(f"Unsupported operand type(s) for +=: 'Currency' and '{type(other).__name__}'")


# ---- Exercise 1 tests ----
if __name__ == "__main__":
    print("=== Exercise 1 ===")
    c1 = Currency('dollar', 5)
    c2 = Currency('dollar', 10)
    c3 = Currency('shekel', 1)
    c4 = Currency('shekel', 10)

    print(c1)           # 5 dollars
    print(int(c1))      # 5
    print(repr(c1))     # 5 dollars
    print(c1 + 5)       # 10
    print(c1 + c2)      # 15
    print(c1)           # 5 dollars

    c1 += 5
    print(c1)           # 10 dollars

    c1 += c2
    print(c1)           # 20 dollars

    # Uncomment to see the required TypeError:
    # print(c1 + c3)
    # TypeError: Cannot add between Currency type <dollar> and <shekel>


