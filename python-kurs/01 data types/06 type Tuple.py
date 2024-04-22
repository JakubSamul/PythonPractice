data=("Ala","Ola","Kasia")
# data[0]="Rafał"

names=data+("Rafał",)
print(names)
print(len(names))
print(type(names))

number=1,2,3
print(type(number))

emptyTuple=()
print(emptyTuple)
print(type(emptyTuple))

print(names[1])
print(names[-1])
print(names[1:3])

cars=(("dodge","ford"),("pontiac"))
print(cars[0][0])

if "ford" in cars[0]:
    print("Ford w kropce nr 1")

del cars

# print(cars)

# del names[0]

tupleX3=names*3
print(tupleX3)