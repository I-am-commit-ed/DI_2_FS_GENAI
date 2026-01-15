from menu_item import MenuItem
from menu_manager import MenuManager

def _read_price(prompt: str) -> int:
    while True:
        raw = input(prompt).strip()
        try:
            price = int(raw)
            if price < 0:
                print("Price must be >= 0.")
                continue
            return price
        except ValueError:
            print("Please enter a valid integer price.")

def add_item_to_menu():
    name = input("Item name: ").strip()
    price = _read_price("Item price: ")

    item = MenuItem(name, price)
    if item.save():
        print("Item was added successfully.")
    else:
        print("Error: item could not be added (maybe it already exists).")

def remove_item_from_menu():
    name = input("Item name to delete: ").strip()

    item = MenuItem(name, 0)
    if item.delete():
        print("Item was deleted successfully.")
    else:
        print("Error: item not found or could not be deleted.")

def update_item_from_menu():
    old_name = input("Current item name: ").strip()
    new_name = input("New item name: ").strip()
    new_price = _read_price("New item price: ")

    item = MenuItem(old_name, 0)
    if item.update(new_name, new_price):
        print("Item was updated successfully.")
    else:
        print("Error: item not found or could not be updated.")

def view_item():
    name = input("Item name to view: ").strip()
    item = MenuManager.get_by_name(name)
    if item is None:
        print("Item not found.")
    else:
        print(f"- {item.name}: {item.price}")

def show_restaurant_menu():
    items = MenuManager.all_items()
    if not items:
        print("Menu is empty.")
        return

    print("\n--- Restaurant Menu ---")
    for it in items:
        print(f"{it.name:<30} {it.price}")
    print("-----------------------\n")

def show_user_menu():
    while True:
        print("Program Menu:")
        print("(V) View an Item")
        print("(A) Add an Item")
        print("(D) Delete an Item")
        print("(U) Update an Item")
        print("(S) Show the Menu")
        print("(E) Exit")

        choice = input("Choose an option: ").strip().upper()

        if choice == "V":
            view_item()
        elif choice == "A":
            add_item_to_menu()
        elif choice == "D":
            remove_item_from_menu()
        elif choice == "U":
            update_item_from_menu()
        elif choice == "S":
            show_restaurant_menu()
        elif choice == "E":
            show_restaurant_menu()
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    show_user_menu()
