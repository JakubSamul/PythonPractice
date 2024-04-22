# Lista

# names_list = []
# names_list.append("Kamil")
# names_list.append("Mariusz")

# print(names_list)

# names_list = ["Kamil", "Mariusz", "Adam", "Kamil"]

# names_list.clear() # usówa z listy wszystkie elementy

# names_list.remove("Kamil") # usówa pierwsze wystąpienie danego elementu
# print(names_list)

# print(names_list)
# print()
# print(names_list.pop(0)) # zwraca elemen z listy i go usówa z listy
# print()
# print(names_list)

# names_list.reverse() # odwraca listę
# names_list.sort() # sortuje listę

# for name in names_list:
#     print(name)

# print(names_list[0]) # konkretny element listy

# print(names_list.count("Rafał")) # liczy ile razy dany element występuję w liście
# print(len(names_list)) # pokazuje długość listy

# mnaes_list2 = ["Dominik"]

# names_list3 = names_list + names_list2
# print(names_list3)

# names_list.sort(reverse=True) # posortowane odwrotnie
# print(names_list)

# Kropka - struktura niemutowalna

# person = ("Jakub","Samul", "29")

# print(person)

# Set - nie wyświetla duplikatów, nie są upożądkowane, muszą być niemutowalne,

# names_set = {"Kamil","Mariusz","Kamil"}

names_set = set()

# names_list = []
# names_tuple = ()

names_set.add("Kamil")  # dodaje element
names_set.add("Mariusz")  # dodaje element
# names_set.add(names_list) # nie można
# names_set.add(names_tuple)

# names_set.remove("Kamil") # usówa element
# names_set.discard("Mariusz") # usówa element


# print(names_set)
names_set2 = {"Mariusz", "Tytus"}

# names_set3 = names_set + names_set2 # błąd nie można setów łączyć za pomocą +

# names_set3 = names_set.union(names_set2) # union twoży nowy set

# names_set.update(names_set2) # updejtuje już istniejący set

# names_set3 = names_set.difference(names_set2) # różnica między dwoma zbiorami - usówa elementy które są w obu setach

# names_set3 = names_set.intersection(names_set2) # część wspólna obu setów

# names_set3 = names_set.symmetric_difference(names_set2) # pokazuje elementy z obu setów ale tylko te które się nie powtażają

# names_set.clear() # czyści set

# for name in names_set3:
#     print(name)

# names_list = ["Artur","Rafał"]

# names_list.extend(names_set2) # dodawanie do listy setu

# print(names_list)

# Dictionary

countries_and_capitals = {"Poland": "Warsaw", "German": "Berlin"}
countries_and_capitals["Czechia"] = "Prague"  # dodawanie nowej wartości

# print(countries_and_capitals)
# for country in countries_and_capitals.keys():
#     print(country)     #   pokazuje klucze

# for capital in countries_and_capitals.values():
#     print(capital)         #     pokazuje wartości

# for country, capital in countries_and_capitals.items():
#     print(country + " - " + capital)       #     pokazuje obie wartości

# print(countries_and_capitals["USA"]) # pokazuje klucz ale jak go nie ma w dictionary to wyskoczy błąd
# print(countries_and_capitals.get("USA")) # pokazuje klucz ale jak go nie ma w dictionary to pokaże None

# print(countries_and_capitals.setdefault("USA", "Washington DC")) # pobiera wartość klucza a jeśli go nie ma to dodaje go do dictionary

# countries_and_capitals.pop("Poland") # usuówa wartość 
# print(countries_and_capitals.pop("Poland")) # usówa i wyświetla wartość usuniętą 
# print(countries_and_capitals.popitem()) # usówa ostatnią dodaną wartość 
# print(countries_and_capitals)

# if "Poland" in countries_and_capitals:
#     print("Znaleziono")
# else:
#     print("Nieznaleziono")

countries_and_capitals.clear() #czyści dictionary
