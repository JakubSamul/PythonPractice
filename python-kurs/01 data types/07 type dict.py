contacts={
    "Ania":"ania@ania.pl",
    "Ola":30,
    "Daniel":"daniel@daniel.com"
}

contacts["Rafał"]="rafal@rafal.pl"

print(contacts["Ola"])
print(contacts["Daniel"])
print(type(contacts))
print(len(contacts))

print(contacts.keys())
print(contacts.values())

for key in contacts:
    print(key+ " " +str(contacts[key]))

print(" ")

for key,value in contacts.items():
    print(key,"",value)