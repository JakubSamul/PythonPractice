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

# names = ["group_a", "group_b", "group_c"]
# values = [1, 10, 100]

# plt.figure(figsize=(9, 3))  # wielkość pojedyńczego okna

# plt.subplot(131)  # słupkowy
# plt.bar(names, values)
# plt.subplot(132)  # punktowy
# plt.scatter(names, values)
# plt.subplot(133)  # liniowy
# plt.plot(names, values)
# plt.suptitle("Categorical Plotting")  # głowna nazwa
# plt.show()

# plt.plot([1, 2, 3, 4], [1, 4, 9, 16], linewidth=5.0)  # grubość lini

# (line,) = plt.plot([1, 2, 3, 4], [1, 4, 9, 16], "-")
# line.set_antialiased(False)  # turn off antialiasing

# lines = plt.plot([1, 2, 3, 4], [1, 4, 9, 16], [1, 2, 3, 4], [2, 4, 6, 8])
# # use keyword arguments
# plt.setp(lines, color="r", linewidth=2.0)
# # # or MATLAB style string value pairs
# # plt.setp(lines, "color", "r", "linewidth", 2.0)

# plt.show()


# def f(t):
#     return np.exp(-t) * np.cos(2 * np.pi * t)


# t1 = np.arange(0.0, 5.0, 0.1)
# t2 = np.arange(0.0, 5.0, 0.02)

# plt.figure()
# plt.subplot(211)
# plt.plot(t1, f(t1), "bo", t2, f(t2), "k")

# plt.subplot(212)
# plt.plot(t2, np.cos(2 * np.pi * t2), "r--")
# plt.show()


# plt.figure(1)  # the first figure
# plt.subplot(211)  # the first subplot in the first figure
# plt.plot([1, 2, 3])
# plt.subplot(212)  # the second subplot in the first figure
# plt.plot([4, 5, 6])


# plt.figure(2)  # a second figure
# plt.plot([4, 5, 6])  # creates a subplot() by default

# plt.figure(1)  # first figure current;
# # subplot(212) still current
# plt.subplot(211)  # make subplot(211) in the first figure
# # current
# plt.title("Easy as 1, 2, 3")  # subplot 211 title

# plt.show()

# mu, sigma = 100, 15
# x = mu + sigma * np.random.randn(10000)

# # the histogram of the data
# n, bins, patches = plt.hist(x, 50, density=True, facecolor="g", alpha=0.75)


# plt.xlabel("Smarts")
# plt.ylabel("Probability")
# # plt.title("Histogram of IQ")
# plt.title(r"$\sigma_i=15$")
# plt.text(60, 0.025, r"$\mu=100,\ \sigma=15$")
# plt.axis([40, 160, 0, 0.03])
# plt.grid(True)
# plt.show()

# ax = plt.subplot()

# t = np.arange(0.0, 5.0, 0.01)
# s = np.cos(2 * np.pi * t)
# (line,) = plt.plot(t, s, lw=2)

# plt.annotate(
#     "local max",  # opis
#     xy=(2, 1),  # co zaznaczmy na wykresie
#     xytext=(3, 1.5),  # gdzie ma być napis
#     arrowprops=dict(facecolor="black", shrink=0.05),  # wygląd strzałki
# )

# plt.ylim(-2, 2)
# plt.show()

# Fixing random state for reproducibility
np.random.seed(19680801)

# make up some data in the open interval (0, 1)
y = np.random.normal(loc=0.5, scale=0.4, size=1000)
y = y[(y > 0) & (y < 1)]
y.sort()
x = np.arange(len(y))

# plot with various axes scales
plt.figure()

# linear
plt.subplot(221)
plt.plot(x, y)
plt.yscale("linear")
plt.title("linear")
plt.grid(True)

# log
plt.subplot(222)
plt.plot(x, y)
plt.yscale("log")
plt.title("log")
plt.grid(True)

# symmetric log
plt.subplot(223)
plt.plot(x, y - y.mean())
plt.yscale("symlog", linthresh=0.01)
plt.title("symlog")
plt.grid(True)

# logit
plt.subplot(224)
plt.plot(x, y)
plt.yscale("logit")
plt.title("logit")
plt.grid(True)
# Adjust the subplot layout, because the logit one may take more space
# than usual, due to y-tick labels like "1 - 10^{-3}"
plt.subplots_adjust(top=0.92, bottom=0.08, left=0.10, right=0.95, hspace=0.25, wspace=0.35)
plt.show()
