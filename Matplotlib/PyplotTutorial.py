import numpy as np

import matplotlib.pyplot as plt

# plt.plot([1, 2, 3, 4], [1, 4, 9, 16]) # rysuje linie pomiedzy punktami (1,1) (2,4) (3,9) (4,16)
# plt.ylabel("some number") # nazwa
# plt.show() # uruchamia wykres

# plt.plot([1, 2, 3, 4], [1, 4, 9, 16], "ro")  # 'ro' - czerwone kropki zamiast lini
# plt.axis((0, 6, 0, 20)) # axis od powiada za minimum i maksimum na osi [xmin, xmax, ymin, ymax]
# plt.show()


# t = np.arange(0.0, 5.0, 0.2)  # wartości od 0 do 5 co 0,2

# plt.plot(t, t, "r--", t, t**2, "bs", t, t**3, "g^")  # czerwone kreski, niebieskie kwadraty, zielone trójkąty
# plt.show()

# data = {"a": np.arange(50), "c": np.random.randint(0, 50, 50), "d": np.random.randn(50)}
# data["b"] = data["a"] + 10 * np.random.randn(50)
# data["d"] = np.abs(data["d"]) * 100

# plt.scatter("a", "b", c="c", s="d", data=data) # pierwsze dwa to dane, s odpowiada za wielkość znaczników a c za kolor
# plt.xlabel("entry a")
# plt.ylabel("entry b")
# plt.show()

names = ["group_a", "group_b", "group_c"]
values = [1, 10, 100]

plt.figure(figsize=(9, 3))  # wielkość pojedyńczego okna

plt.subplot(131)  # słupkowy
plt.bar(names, values)
plt.subplot(132)  # punktowy
plt.scatter(names, values)
plt.subplot(133)  # liniowy
plt.plot(names, values)
plt.suptitle("Categorical Plotting")  # głowna nazwa
plt.show()
