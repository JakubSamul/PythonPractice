def float_to_string_converter(value: float) -> str:
    if value == float("inf"):
        return "inf"  # nieskonczonosc
    elif value == float("-inf"):
        return "-inf"
    elif value != value:
        return "NaN"  # Not a number

    if value == int(value):
        return f"{int(value):,}".replace(",", " ")
    else:
        return f"{value:,}".replace(",", " ")
