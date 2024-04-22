
from pyparsing import countedArray


countries_and_capitals = {"Poland":"Warsaw","Czechia":"Prague","Germany":"Berlin"}


try:
    print(2/2)
    print(countries_and_capitals["USA"])
except KeyError:
    print("Klucz nie został znaleziony")
except ZeroDivisionError:
    print("Nie można dzielić przez zero")
finally:
    print("To wykona się zawsze")

print("Jestem tutaj")
