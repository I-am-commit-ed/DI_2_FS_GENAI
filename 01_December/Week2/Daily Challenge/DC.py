class Farm:
    def __init__(self, farm_name: str):
        self.name = farm_name
        self.animals = {}  # e.g. {"cow": 1, "pig": 3, "horse": 2}

    def add_animal(self, animal_type: str = None, count: int = 1, **kwargs):
        """
        Supports BOTH styles:

        1) Single animal:
           add_animal("cow", 5)
           add_animal("sheep")  # default count = 1

        2) Multiple animals via kwargs:
           add_animal(cow=5, sheep=2, goat=12)

        Note: Python does NOT allow 'cow'=5 (quotes) in kwargs. Use cow=5.
        """
        # kwargs style: add_animal(cow=5, sheep=2, goat=12)
        if kwargs:
            for a_type, a_count in kwargs.items():
                if not isinstance(a_count, int) or a_count < 1:
                    raise ValueError(f"Count for '{a_type}' must be a positive integer.")
                self.animals[a_type] = self.animals.get(a_type, 0) + a_count
            return

        # single animal style: add_animal("cow", 5)
        if animal_type is None:
            raise ValueError("Provide animal_type/count or pass animals as keyword arguments.")

        if not isinstance(count, int) or count < 1:
            raise ValueError("count must be a positive integer.")

        self.animals[animal_type] = self.animals.get(animal_type, 0) + count

    def get_info(self) -> str:
        # Align animal names into a neat column based on the longest key
        width = max((len(a) for a in self.animals), default=0)
        lines = [f"{self.name}'s farm", ""]
        for animal, qty in self.animals.items():
            lines.append(f"{animal.ljust(width)} : {qty}")
        lines.extend(["", "    E-I-E-I-0!"])
        return "\n".join(lines)

    def get_animal_types(self):
        return sorted(self.animals.keys())

    def get_short_info(self) -> str:
        animal_types = self.get_animal_types()
        pluralized = []
        for a in animal_types:
            qty = self.animals.get(a, 0)
            pluralized.append(a + ("s" if qty > 1 else ""))

        if not pluralized:
            animals_part = "no animals"
        elif len(pluralized) == 1:
            animals_part = pluralized[0]
        elif len(pluralized) == 2:
            animals_part = f"{pluralized[0]} and {pluralized[1]}"
        else:
            animals_part = ", ".join(pluralized[:-1]) + f" and {pluralized[-1]}"

        return f"{self.name}'s farm has {animals_part}."

# -------------------------
# Test the code (required)
# -------------------------
macdonald = Farm("McDonald")
macdonald.add_animal('cow', 5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)

print(macdonald.get_info())
print()
print(macdonald.get_short_info())

# Bonus kwargs usage:
# macdonald2 = Farm("McDonald")
# macdonald2.add_animal(cow=5, sheep=2, goat=12)
# print(macdonald2.get_info())
