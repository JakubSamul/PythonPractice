
print("Hello" + "World!")
print("Hello" * 3)

string = "Hello World!"
print(string[0])  # H
print(string[0:5])  # Hello

print("Hello" in string)  # True
print("Hello" not in string)  # False

multiline = """line1
line2
line3
"""

print("ala".capitalize())  # Ala
print("Ola ma kota, Ola ma psa".count("Ola"))  # 2

print("Hello".center(20, "-"))  # -------Hello--------

print(string.startswith("Hello"))  # True
print(string.endswith("World!"))  # True

print(string.find("Ola"))  # -1 nie występuje
print(string.find("World"))  # 6
print("Ola ma psa, Ola ma kota".rfind("Ola"))  # 12 od końca szuka

print("2377577".isalnum())  # True
print("2377577.".isalnum())  # False
print("2377577 k".isalnum())  # False

print("2377577 k".isalpha())  # False
print("kot ".isalpha())  # False bo spacja
print("kot".isalpha())  # True
print("kot2".isalpha())  # False

print("test".islower())  # True
print("tesT".islower())  # False

print("TEST".isupper())  # True

print("TEST".isspace())  # False
print(" \n\t\n".isspace())  # True

print("-|".join(["Ala", "Ola", "Adam"]))  # Ala-|Ola-|Adam

print("Hello World!".lower())  # hello world!
print("Hello World!".upper())  # HELLO WORLD!
print("Hello World!".swapcase())  # hELLO wORLD!

print("   \n \t Hello World \n \t  \n".lstrip())
print("   \n \t Hello World \n \t  \n".rstrip())
print("   \n \t Hello   World \n \t  \n".strip())

# Kasia ma psa, Kasia ma kota
print("Ola ma psa, Ola ma kota".replace("Ola", "Kasia"))

print("My name is {myName}, I'm from {country}".format(
    myName="Kuba", country="Poland"))  # My name is Kuba, I'm from Poland
print("My name is {myName}, my postal code is {code}".format(
    myName="Kuba", code=12345))  # My name is Kuba, my postal code is 12345
# My name is Kuba, my postal code is 12345
print("My name is {0}, my postal code is {1}".format("Kuba", 12345))
# My name is Kuba, my postal code is 12345
print("My name is {}, my postal code is {}".format("Kuba", 12345))
