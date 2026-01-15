from db_config import get_connection
from menu_item import MenuItem

class MenuManager:
    @classmethod
    def get_by_name(cls, name: str):
        """
        Return a MenuItem if found, else None.
        """
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    "SELECT item_name, item_price FROM menu_items WHERE item_name = %s",
                    (name,),
                )
                row = cur.fetchone()

        if not row:
            return None

        return MenuItem(row["item_name"], row["item_price"])

    @classmethod
    def all_items(cls):
        """
        Return a list of MenuItem objects.
        """
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    "SELECT item_name, item_price FROM menu_items ORDER BY item_name ASC"
                )
                rows = cur.fetchall()

        return [MenuItem(r["item_name"], r["item_price"]) for r in rows]
