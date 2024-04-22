
data = {"name": "Ola", "city": "Waw"}

print(data["name"])  # Ola
dataPostalCode = "postalCode"
data[dataPostalCode] = 1234
print(data)  # {'name': 'Ola', 'city': 'Waw', 'postalCode': 1234}
print(len(data))

del data["city"]
print(data)  # {'name': 'Ola', 'postalCode': 1234}
data.clear()
print(data)  # {}

data = {"name": "Kasia", "city": "Krk"}
dataCopy = data.copy()
print(dataCopy)
# True te same miejsce w pamięci - płytka kopia, ale tylko do elementów listy
print(data["name"] is dataCopy["name"])
print(data is dataCopy)  # False dwa różne miejsca w pamięci

data2 = dict.fromkeys(("name", "city", "code"))
print(data2)

data3 = dict.fromkeys(("name", "city", "code"), 0)
print(data3)

print(data2.get("x", "DEFAULT"))

print("name" in data2) #True

print(data2.keys())
print(data2.values())
