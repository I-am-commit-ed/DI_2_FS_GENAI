# -----------------------------
# Challenge 1: Letter Index Dictionary
# -----------------------------
word = input("Enter a word: ")

letter_indexes = {}
for i, ch in enumerate(word):
    if ch in letter_indexes:
        letter_indexes[ch].append(i)
    else:
        letter_indexes[ch] = [i]

print(letter_indexes)


# -----------------------------
# Challenge 2: Affordable Items
# -----------------------------
def money_to_int(money_str: str) -> int:
    # Removes $ and commas (no hard-coding specific numbers)
    cleaned = money_str.replace("$", "").replace(",", "").strip()
    return int(cleaned)

def affordable_items(items_purchase: dict, wallet: str):
    budget = money_to_int(wallet)
    basket = []

    # Buy in dictionary order = priority (Python 3.7+ preserves insertion order)
    for item, price_str in items_purchase.items():
        price = money_to_int(price_str)
        if price <= budget:
            basket.append(item)
            budget -= price

    if not basket:
        return "Nothing"
    return sorted(basket)

# --- Example tests ---
items_purchase_1 = {"Water": "$1", "Bread": "$3", "TV": "$1,000", "Fertilizer": "$20"}
wallet_1 = "$300"
print(affordable_items(items_purchase_1, wallet_1))  # ["Bread", "Fertilizer", "Water"]

items_purchase_2 = {"Apple": "$4", "Honey": "$3", "Fan": "$14", "Bananas": "$4", "Pan": "$100", "Spoon": "$2"}
wallet_2 = "$100"
print(affordable_items(items_purchase_2, wallet_2))  # ["Apple", "Bananas", "Fan", "Honey", "Spoon"]

items_purchase_3 = {"Phone": "$999", "Speakers": "$300", "Laptop": "$5,000", "PC": "$1200"}
wallet_3 = "$1"
print(affordable_items(items_purchase_3, wallet_3))  # "Nothing"
