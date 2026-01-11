"""
Old MacDonald’s Farm — COPY/PASTE READY

Implements:
- Farm.__init__(farm_name)
- Farm.add_animal(...)  (supports: add_animal("cow", 5) AND add_animal(cow=5, sheep=2))
- Farm.get_info()
Bonus:
- Farm.get_animal_types()
- Farm.get_short_info()
"""

from __future__ import annotations


class Farm:
    def __init__(self, farm_name: str):
        self.name = farm_name
        self.animals = {}  # e.g. {"cow": 5, "sheep": 2}

    def add_animal(self, animal_type: str = None, count: int = 1, **kwargs):
        """
        Supports BOTH calling styles:

        1) Single animal (original requirement):
            add_animal("cow", 5)
            add_animal("sheep")  # default count = 1

        2) Multiple animals (bonus kwargs):
            add_animal(cow=5, sheep=2, goat=12)

        Notes:
        - If both positional and kwargs are provided, both will be applied.
        """
        # Handle single animal style
        if animal_type is not None:
            if not isinstance(animal_type, str) or not animal_type.strip():
                raise ValueError("animal_type must be a non-empty string")
            if not isinstance(count, int) or count < 1:
                raise ValueError("count must be an integer >= 1")

            self.animals[animal_type] = self.animals.get(animal_type, 0) + count

        # Handle kwargs style
        for animal, qty in kwargs.items():
            if not isinstance(animal, str) or not animal.strip():
                raise ValueError("Animal names in kwargs must be non-empty strings")
            if not isinstance(qty, int) or qty < 1:
                raise ValueError("Animal quantities in kwargs must be integers >= 1")

            self.animals[animal] = self.animals.get(animal, 0) + qty

    def get_info(self) -> str:
        """
        Returns a formatted string matching the example output.
        Uses a simple aligned layout with "animal : count".
        """
        lines = [f"{self.name}'s farm", ""]

        # Optional: stable output by sorting animal names
        for animal in sorted(self.animals.keys()):
            lines.append(f"{animal} : {self.animals[animal]}")

        lines.append("")
        lines.append("    E-I-E-I-0!")
        return "\n".join(lines)

    # -------------------------
    # Bonus methods
    # -------------------------
    def get_animal_types(self):
        return sorted(self.animals.keys())

    def get_short_info(self) -> str:
        """
        Example:
        "McDonald's farm has cows, goats and sheeps."
        """
        animal_types = self.get_animal_types()
        if not animal_types:
            return f"{self.name}'s farm has no animals."

        # pluralize based on count > 1
        names = []
        for animal in animal_types:
            if self.animals.get(animal, 0) > 1:
                names.append(animal + "s")
            else:
                names.append(animal)

        # join with commas and "and"
        if len(names) == 1:
            animals_part = names[0]
        elif len(names) == 2:
            animals_part = f"{names[0]} and {names[1]}"
        else:
            animals_part = ", ".join(names[:-1]) + f" and {names[-1]}"

        return f"{self.name}'s farm has {animals_part}."


# -------------------------
# Tests (as in the prompt)
# -------------------------
if __name__ == "__main__":
    macdonald = Farm("McDonald")
    macdonald.add_animal('cow', 5)
    macdonald.add_animal('sheep')
    macdonald.add_animal('sheep')
    macdonald.add_animal('goat', 12)

    print(macdonald.get_info())
    # Expected:
    # McDonald's farm
    #
    # cow : 5
    # sheep : 2
    # goat : 12
    #
    #     E-I-E-I-0!

    print()
    print(macdonald.get_short_info())
    # Example:
    # McDonald's farm has cows, goats and sheeps.

    print("\nBonus kwargs add_animal:")
    macdonald2 = Farm("McDonald")
    macdonald2.add_animal(cow=5, sheep=2, goat=12)
    print(macdonald2.get_info())
    
macdonald.add_animal(cow=5, sheep=2, goat=12)
