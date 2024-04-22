setData={2,3,4,6,7}
setData.add(22)

setData.discard(2)
print(type(setData))
print(setData)

for v in setData:
    print(v)

frozenData=frozenset(setData)
print(type(frozenData))
# frozenData.add(33) = błąd

for value in frozenData:
    print(value)