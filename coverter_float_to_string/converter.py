import tkinter as tk


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


def convert():
    try:
        value = float(entry.get())
        result.set(float_to_string_converter(value))
    except ValueError:
        result.set("Błąd: Wprowadź prawidłową liczbę.")


# aplikacja
root = tk.Tk()
root.title("Konwerter Float na String")

# układ elementów
frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

# wprowadzanie danych
label = tk.Label(frame, text="Wprowadź liczbę float:")
label.grid(row=0, column=0)

entry = tk.Entry(frame)
entry.grid(row=0, column=1)

# przycisk do wykonania konwersji
button = tk.Button(frame, text="Konwertuj", command=convert)
button.grid(row=1, column=0, columnspan=2)

# wyświetlanie wyniku
result = tk.StringVar()
result_label = tk.Label(frame, textvariable=result)
result_label.grid(row=2, column=0, columnspan=2)

root.mainloop()
