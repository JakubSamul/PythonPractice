from operator import truediv, mul, add, sub

# def add(a,b):
#    return a + b

# def subtract(a, b):
#    return a - b

# def multiply(a, b):
#    return a * b

# def divide(a, b):
#    return a / b


def calc(operator, a, b):
    operators = {"+": add, "-": sub, "*": mul, "/": truediv}
    method = operators.get(operator, lambda a, b: None)
    if method:
        return method(a, b)
    else:
        return None


def calculator():
    operation = None
    allowed_operations = ["+", "-", "*", "/"]
    while operation not in allowed_operations:
        operation = input(
            """
        Podaj operację jaką chcesz wykonać
        + dodawanie
        - odejmowanie
        * mnożenie
        / dzielenie
        """
        )

    a = float(input("Podaj pierwszą liczbę: "))
    b = float(input("Podaj drugą liczbę: "))
    try:
        result = calc(operation, a, b)
    except ZeroDivisionError:
        print("Nie można dzielić przez zero")
    else:
        print(result if result is not None else "Niedozwolona operacja")
