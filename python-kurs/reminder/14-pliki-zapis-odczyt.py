
file = open("countries_and_capitals.txt","w+") 
# r - plik do odczytu
# w - plik do zapisu
# w+ - plik do odczytu i do zapisu 

countries_and_capitals = {"Poland":"Warsaw","Czechia":"Prague","Germany":"Berlin"}

for country, capital in countries_and_capitals.items():
    file.write(country + " - " + capital + "\n")
# write - zapisuje to w pliku który został stworzony

file.close()


###

file = open("countries_and_capitals.txt")

for line in file.readlines():
    # readlines - czyta wszystkie linie 
    print(line.strip())
    # usówa wszystkie odstępy 

file.close()
