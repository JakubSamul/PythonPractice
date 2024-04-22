countries_information = {}
countries_information["Polska"] = ("Warszawa", 37.97)
countries_information["Niemcy"] = ("Berlin", 87.02)
countries_information["Słowacja"] = ("Bratysława", 5.45)
# print(countries_information)

def show_country_info(country):
    country_information = countries_information.get(country)

    print()
    print(country)
    print("------------")
    print("Stolica: " + country_information[0])
    print("Liczba mieszkańców w milionach: " + str(country_information[1]))


for country in countries_information.keys():
    print(country)

country = input("Informację o jakim kraju chcesz wyświetlić ? ")
show_country_info(country)



