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
        return f"{value:,}".replace(",", " ")


print(float_to_string_converter(2000000.22))
print(float_to_string_converter(875867843675.55533))
print(float_to_string_converter(0.0000000000012))
