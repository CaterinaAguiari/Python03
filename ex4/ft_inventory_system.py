import sys
print("=== Inventory System Analysis ===")
if len(sys.argv) == 1:
    print("Error: no arguments provided!")
    sys.exit(1)
else:
    inventory: dict = {}
    for arg in sys.argv[1:]:
        if ":" not in arg:
            print(f"Error - invalid parameter '{arg}'")
            continue
        parts: list[str] = arg.split(":", 1)
        key: str = parts[0].strip()
        value_str: str = parts[1].strip()

        if not key:
            print(f"Error - empty key in '{arg}'")
            continue
        try:
            value: int = int(value_str)
        except ValueError as e:
            print(f"Quantity error for '{key}': {e}")
            continue

        if key in inventory:
            print(f"Redundant item '{key}' - discarding")
            continue

        inventory[key] = value

print(f"Got inventory: {inventory}")
items: list[str] = list(inventory.keys())
print(f"Item list: {items}")
tot_items: int = sum(inventory.values())
count: int = 0
for object in inventory:
    count += 1
print(f"Total quantity of the {count} items: {tot_items}")
for object, quantity in inventory.items():
    percentage: float = (quantity / tot_items) * 100
    print(f"Item {object} represents {percentage:.1f}%")
most_abundant: str = items[0]
least_abundant: str = items[0]
for item in items:
    if inventory[item] > inventory[most_abundant]:
        most_abundant = item
    if inventory[item] < inventory[least_abundant]:
        least_abundant = item
print(f"Item most abundant: {most_abundant}"
      f"with quantity {inventory[most_abundant]}"
      )
print(f"Item least abundant: {least_abundant}"
      f"with quantity {inventory[least_abundant]}"
      )
new_item: dict[str, int] = {"new": 1}
inventory.update(new_item)
print(f"Update inventory: {inventory}")
