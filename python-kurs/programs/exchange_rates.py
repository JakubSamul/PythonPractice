import requests

r = requests.get("http://api.nbp.pl/api/exchangerates/tables/a?format=json")

if r.ok == True:
    data = r.json()[0]
    print(data)

    table = data["table"]
    no = data["no"]
    effectiveDate = data["effectiveDate"]
    print("\nExchange rate", table , no , effectiveDate)

    rates = data["rates"]

    for rate in rates:
        currency = rate["currency"]
        code = rate["code"]
        mid = rate["mid"]
        print(currency, "code:", code, "value:", mid)


def greet(name):
    print(f"wiaj {name}")

greet("dawid")

ala = 'Alice'
dawid  = "Dave"
kuba = "Jacob"
name = "Alicja: " + ala + " Dawid: " + dawid + " Kuba: " + kuba

name = f"Alicja {ala} Dawid: {dawid} Kuba: {kuba}"
print(name)