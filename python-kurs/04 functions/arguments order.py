

def printCar(brand,/, name="concept",*,year=1960,color="black"):
    print(brand,name,year,color)

printCar("Ford","Mustang",year=1973,color="Blue")
printCar("Ford","Mustang",color="Blue",year=1973)
printCar("Ford",name="Mustang",color="Blue",year=1973)
# printCar("Ford",name="Mustang",color="Blue",1973) błąd
# printCar("Ford",name="Mustang","Blue",year=1973) błąd
# printCar(brand="Ford","Mustang",color="Blue",year=1973) błąd


