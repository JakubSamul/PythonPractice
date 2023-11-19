def headline(text: str, align: bool = True) -> str:
    if align:
        return f"{text.title()}\n{'-' * len(text)}"
    else:
        return f" {text.title()} ".center(50, "o")



# print(headline("python type checking", align="left"))

# print(headline("python type checking", align="center"))

print(headline("python type checking", align=False))