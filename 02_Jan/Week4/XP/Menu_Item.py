from db_config import get_connection

class MenuItem:
    def __init__(self, name: str, price: int = 0):
        self.name = name
        self.price = price

    def save(self) -> bool:
        """
        Insert this item into menu_items.
        Returns True if inserted, False otherwise (e.g., duplicate name).
        """
        try:
            with get_connection() as conn:
                with conn.cursor() as cur:
                    cur.execute(
                        """
                        INSERT INTO menu_items (item_name, item_price)
                        VALUES (%s, %s)
                        """,
                        (self.name, self.price),
                    )
            return True
        except Exception:
            return False

    def delete(self) -> bool:
        """
        Delete the item by name.
        Returns True if a row was deleted, False if not found.
        """
        try:
            with get_connection() as conn:
                with conn.cursor() as cur:
                    cur.execute(
                        "DELETE FROM menu_items WHERE item_name = %s",
                        (self.name,),
                    )
                    return cur.rowcount > 0
        except Exception:
            return False

    def update(self, new_name: str, new_price: int) -> bool:
        """
        Update this item (by current self.name) to new name + new price.
        Returns True if updated, False if not found or error.
        """
        try:
            with get_connection() as conn:
                with conn.cursor() as cur:
                    cur.execute(
                        """
                        UPDATE menu_items
                        SET item_name = %s, item_price = %s
                        WHERE item_name = %s
                        """,
                        (new_name, new_price, self.name),
                    )
                    updated = cur.rowcount > 0

            if updated:
                # update the object too
                self.name = new_name
                self.price = new_price

            return updated
        except Exception:
            return False
