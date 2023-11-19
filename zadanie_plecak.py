from dataclasses import dataclass

@dataclass
class Item:
    weight: int
    value: int
    
watch = Item(25,75)
ring = Item(26,90)
book = Item(51,200)

print(watch, ring, book)

# # def pack_backpack(items: list[Item], weight):
# #     pass

# def fu(a):
#     print(a,10)
#     if a <= 0:
#         return 0 
#     else:
#         return 10 + fu(a-1)
# # a = 5 w 10 = w4
# # a = 4 w 10 + 10 + w3
# print("sdas",fu(5))


# print(suma(5))

# def suma(a):
#     if a < 0:
#         return 0 
#     else:
#         return a + suma(a-1)

# print(suma(5))
    # 0+1+2+3+4+5   5+4+3+2+1+0

