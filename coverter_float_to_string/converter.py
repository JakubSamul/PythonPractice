def float_to_string_converter(value: float) -> str:
    if value == float("inf"):
        return "inf"
    elif value == float("-inf"):
        return "-inf"
    elif value != value:
        return "NaN"  # Not a number

    if value == int(value):
        return f"{int(value):,}".replace(",", " ")
    else:
        return f"{value:,.2f}".replace(",", " ")


print(float_to_string_converter(2000000.22))
print(float_to_string_converter(200000.228))
print(float_to_string_converter(2000))
