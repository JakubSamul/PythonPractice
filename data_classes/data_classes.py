from dataclasses import dataclass

@dataclass
class Item:
    weight: int
    value: int

watch = Item(2,5)
ring = Item(1,10)
book = Item(5,3)

print(watch, ring, book)