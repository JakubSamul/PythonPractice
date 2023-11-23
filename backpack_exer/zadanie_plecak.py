from dataclasses import dataclass

@dataclass
class Item:
    name: str
    weight: int
    value: int
    
watch = Item('watch',3,7)
bracelet = Item('bracelet',2,3)
earrings = Item('earrings',1,2)


def pack_backpack(items: list[Item], weight: int) -> int:
    max_val = 0
    val = []
    for i in items:
        if weight - i.weight < 0:
            break
        else:
            max_val = i.value + pack_backpack([earrings, bracelet, watch], weight-i.weight)
            val.append(max_val)
            print(max(val))
    print(val)
    if val:
        return max(val)
    else:
        return 0
        

print(pack_backpack([earrings, bracelet, watch],5))

def test(packed: list[Item], avaliable: list[Item], size: int) -> list[Item]:
    for item in avaliable:
        if item.weight <= size:
            return test(packed + [item], avaliable, size - item.weight)
    return packed

print(test([], [earrings, bracelet, watch], 10))
     

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

