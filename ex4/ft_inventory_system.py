#!/usr/bin/env python3
import sys

def main() -> None:
    print("=== Inventory System Analysis ===\n")
    dic: dict[str, int] = {}
    argc: int = len(sys.argv)
    for item in sys.argv[1:]:
        parts: list[str] = item.split(":")
        if len(parts) == 2:
            name, quant = parts

            if name in dic:
                print(f"Redundant item ’{name}’ - discarding")
                continue
            try:
                real_quant = int(quant)
            except ValueError:
                print(f"Quantity error for ’{name}’: invalid literal for int() with base 10:’{quant}’")
                continue
        else:
            print(f"Error - invalid parameter ’{item}’")

        dic[name] = real_quant
    print(f"Got inventory: {dic}")
    print(f"Item list:{list(dic)}")
    total: int = sum(dic.values())
    items_num: int = len(dic)
    print(f"Total quantity of the {items_num} items: {total}")
    for item in dic:
        percent: float = round((dic[item] / total) * 100, 1)
        print(f"Item {item} represents  {percent}%")

    max_name = ""
    max_value = -1
    for name in dic:
        if dic[name] > max_value:
            max_value = dic[name]
            max_name = name

print(f"Item most abundant: {max_name} with quantity {max_value}")

min_name = ""
min_value = 10**9

for name in dic:
    if dic[name] < min_value:
        min_value = dic[name]
        min_name = name

print(f"Item least abundant: {min_name} with quantity {min_value}")

dic.update({"magic_item": 1})
print(f"Updated inventory: {dic}")
if __name__ == "__main__":
    main()
