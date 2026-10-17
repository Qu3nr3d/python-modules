from sys import argv


def check_duplicate(inv: dict[str, int], item: str) -> bool:
    for key in inv:
        if key == item:
            return True
    return False


def create_dic() -> dict[str, int]:
    inventory = argv[1:]
    inventory_dict: dict[str, int] = {}

    for arg in inventory:
        item: str = ""
        quantity: str = ""
        found_colon: int = 0
        for i in range(len(arg)):
            if arg[i] == ":":
                found_colon += 1
                item = arg[:i]
                quantity = arg[i + 1:]
        if found_colon != 1 or item == "" or quantity == "":
            print(f"Error - Invalid parameter '{arg}'")
            continue
        try:
            quantityy: int = int(quantity)
        except Exception as e:
            print(f"Quantity error for '{item}': {e}")
            continue
        if check_duplicate(inventory_dict, item):
            print(f"Redundant item '{item} - discarding")
            continue
        inventory_dict.update({item: quantityy})
    return inventory_dict


def add_item(inv: dict[str, int]) -> None:
    inv.update({"magic_item": 1})


if __name__ == "__main__":
    print("=== Inventory System Analysis ===")
    inv = create_dic()
    print(f"Got inventory: {inv}")
    print(f"Total quantity of the {len(inv)}: {sum(inv.values())}")
    try:
        max_quanity = {list(inv.keys())[0]: list(inv.values())[0]}
        min_quanity = {list(inv.keys())[0]: list(inv.values())[0]}
        for key in inv:
            value = inv[key]
            if value > list(max_quanity.values())[0]:
                max_quanity = {key: value}
            elif value < list(min_quanity.values())[0]:
                min_quanity = {key: value}
            print(f"Item {key} represents "
                  f"{round((value/sum(inv.values()) * 100), 1)}%")
        max_item = list(max_quanity.keys())[0]
        max_quantity = list(max_quanity.values())[0]

        min_item = list(min_quanity.keys())[0]
        min_quantity = list(min_quanity.values())[0]

        print(f"Item most abundant: {max_item} with quantity {max_quantity}")
        print(f"Item least abundant: {min_item} with quantity {min_quantity}")
        add_item(inv)
        print(f"Updated inventory: {inv}")
    except Exception:
        print("inventory is empty!")
