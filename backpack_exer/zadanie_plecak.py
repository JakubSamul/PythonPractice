from dataclasses import dataclass


@dataclass
class Item:
    name: str
    weight: int
    value: int


watch = Item("watch", 3, 7)
bracelet = Item("bracelet", 2, 3)
earrings = Item("earrings", 1, 2)


def pack_backpack(
    finish: [], thing: [], result: [], packed: [], items: list[Item], weight: int
) -> str:
    print("pack_backpack")
    for i in items:
        print(i)
        if weight - i.weight < 0:
            if len(result) < 1:
                result += [packed]
                finish += [thing]
            elif len(result) == 1:
                if sum(result[0]) < sum(packed):
                    result[0] = packed
                    finish[0] = thing
            break
        else:
            pack_backpack(
                finish,
                thing + [i.name],
                result,
                packed + [i.value],
                items,
                weight - i.weight,
            )
    return (
        "Musisz spakować "
        + str(finish[0])
        + " plecak będzie miał wtedy wartość "
        + str(sum(result[0]))
    )


print(pack_backpack([], [], [], [], [earrings, bracelet, watch], 25))

# def test(packed: list[Item], avaliable: list[Item], size: int) -> list[Item]:
#     for item in avaliable:
#         if item.weight <= size:
#             return test(packed + [item], avaliable, size - item.weight)
#     return packed

# # print(test([], [earrings, bracelet, watch], 10))


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
