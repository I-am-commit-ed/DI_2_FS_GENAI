import math
from typing import Any, List, Optional


class Pagination:
    def __init__(self, items: Optional[List[Any]] = None, page_size: int = 10):
        if page_size <= 0:
            raise ValueError("page_size must be >= 1")

        self.items: List[Any] = items if items is not None else []
        self.page_size: int = page_size
        self.current_idx: int = 0  # 0-based page index

        # Total pages (0 if no items)
        self.total_pages: int = math.ceil(len(self.items) / self.page_size) if self.items else 0

    def get_visible_items(self) -> List[Any]:
        start = self.current_idx * self.page_size
        end = start + self.page_size
        return self.items[start:end]

    def go_to_page(self, page_num: int) -> "Pagination":
        # page_num is 1-based from user perspective
        if self.total_pages == 0:
            raise ValueError("No pages available (items list is empty).")

        if page_num < 1 or page_num > self.total_pages:
            raise ValueError(f"page_num must be between 1 and {self.total_pages}, got {page_num}")

        self.current_idx = page_num - 1
        return self  # allows chaining

    def first_page(self) -> "Pagination":
        self.current_idx = 0
        return self

    def last_page(self) -> "Pagination":
        self.current_idx = max(self.total_pages - 1, 0)
        return self

    def next_page(self) -> "Pagination":
        if self.total_pages > 0:
            self.current_idx = min(self.current_idx + 1, self.total_pages - 1)
        return self

    def previous_page(self) -> "Pagination":
        self.current_idx = max(self.current_idx - 1, 0)
        return self

    def __str__(self) -> str:
        return "\n".join(str(x) for x in self.get_visible_items())


# ----------------------------
# Tests (from the instructions)
# ----------------------------
if __name__ == "__main__":
    alphabetList = list("abcdefghijklmnopqrstuvwxyz")
    p = Pagination(alphabetList, 4)

    print(p.get_visible_items())
    # ['a', 'b', 'c', 'd']

    p.next_page()
    print(p.get_visible_items())
    # ['e', 'f', 'g', 'h']

    p.last_page()
    print(p.get_visible_items())
    # ['y', 'z']

    try:
        p.go_to_page(10)
        print(p.current_idx + 1)
    except ValueError as e:
        print("ValueError:", e)

    try:
        p.go_to_page(0)
    except ValueError as e:
        print("ValueError:", e)

    # Bonus chaining example:
    p2 = Pagination(alphabetList, 4)
    print(p2.next_page().next_page().next_page().get_visible_items())
    # ['m', 'n', 'o', 'p']

    # Bonus __str__ example:
    p3 = Pagination(alphabetList, 4)
    print(str(p3))
    # a
    # b
    # c
    # d
