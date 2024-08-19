import numpy as np

# a = [1, 2, 3, 4, 5]
# print(a)
# print(a[1])
# print(a[1:3])
# print(a[-1])

# a = np.array([1, 2, 3, 4, 5])
# print(a)
# print(a[1])
# print(a[1:3])
# print(a[-1])
# a[2] = 100
# print(a)

# a_nul = np.array(
#     [
#         [[1, 2, 3, 1], [4, 5, 6, 1], [7, 8, 9, 1]],
#         [[1, 2, 3, 1], [4, 5, 6, 1], [7, 8, 9, 1]],
#     ]
# )
# print(a_nul[0])
# print(a_nul[0, 1])
# print(a_nul.shape)
# print(a_nul.ndim)
# print(a_nul.size)
# print(a_nul.dtype)

# Data Types

# a_niedziala = np.array(
#     [[1, 2, 3], [4, "hello", 6], [7, 8, 9]], dtype=np.int32
# )  # z 'hello' nie da się zrobić int32
# a = np.array([[1, 2, 3], [4, "5", 6], [7, 8, 9]], dtype=np.int32)
# print(a.dtype)
# print(a[1][1].dtype)
# print(a[1, 1])

# d = {"1": "A"}
# a = np.array([[1, 2, 3], [4, d, 6], [7, 8, "hello"]])
# print(a.dtype)
# print(type(a[1][1]))

# a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]], dtype="<U7")
# print(a.dtype)
# print(type(a[1][0]))


# Filling Arrays

# a = np.full((3, 3, 3), 7)
# print(a)

# a = np.zeros((3, 3, 3))
# print(a)

# a = np.ones((3, 3, 3))
# print(a)

# a = np.empty((3, 3, 3))
# print(a)

# x_values = np.arange(0, 1000, 5)
# print(x_values)

# x_values = np.linspace(0, 1000, 1001)
# print(x_values)


# NaN and Infinity

# print(np.nan)
# print(np.inf)
# print(np.isnan(np.sqrt(-1)))
# print(np.isinf(np.array([10]) / 0))


# Mathemathical Operations

# l1 = [1, 2, 3, 4, 5]
# l2 = [6, 7, 8, 9, 0]
# a1 = np.array(l1)
# a2 = np.array(l2)
# print(l1 * 5)
# print(a1 * 5)
# print(l1 + 5) # nie działa
# print(a1 + 5)
# print(l1 + l2)  # dodawanie list
# print(a1 + a2) # dodawanie element po elemencie,
#                # możemy to samo zrobić z innymi operacjami
# a1 = np.array(
#     [
#         1,
#         2,
#         3,
#     ]
# )
# a2 = np.array([[1], [2]])
# print(a1 + a2)  # muszą być kompatybilne wymiary
# wszystkie funkcje matematyczne są dostępne w numpy
# https://numpy.org/doc/stable/reference/routines.math.html


# Array Methods

# a = np.array([1, 2, 3, 4, 5])
# a = np.append(a, [6, 7, 8])  # dodaje elementy na końcu
# a = np.insert(a, 1, [2, 2, 2, 2])  # dodaje elementy na danej pozycji
# print(a)
# a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# print(np.delete(a, 0, 0))  # usuwa elementy z danej pozycji
# print(np.delete(a, 1, 1))


#  Structuring Methods

# a = np.array(
#     [
#         [1, 2, 3, 4, 5],
#         [6, 7, 8, 9, 10],
#         [11, 12, 13, 14, 15],
#         [16, 17, 18, 19, 20],
#     ]
# )
# print(a.shape)
# print(a.reshape(5, 4))  # zmienia wymiary
# print(
#     a.reshape(
#         20,
#     )
# )
# print(a.reshape(20, 1))
# print(a.reshape(2, 10))
# print(a.reshape(2, 2, 5))
# print(a.reshape(2, 5, 2))
# print(a.reshape(5, 2, 2))
# print(a.reshape(2, 2, 1, 5, 1))
# a.reshape(10, 2) # zmienia wymiary, ale nie zapisuje
# print(a)
# a.resize(10, 2) # zmienia wymiary i zapisuje
# print(a)
# print(
#     a.flatten()
# )  # spłaszcza tablicę ale nie zmienia tego w orginalnej tablicy
# print(a.ravel())  # spłaszcza tablicę i zmienia to w orginalnej tablicy
# var1 = a.flatten()
# var1[2] = 100
# print(var1)
# print(a)
# var2 = a.ravel()
# var2[2] = 200
# print(var1)
# print(a)
# var = [v for v in a.flat]
# print(var)  # zwraca iterator, który można przekonwertować na listę
# print(a.transpose())  # transponuje tablicę
# print(a.T)  # to samo co wyżej
# print(a.swapaxes(0, 1))  # zamienia osie


# Concatenating, Stacking, Splitting

# a1 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
# a2 = np.array([[11, 12, 13, 14, 15], [16, 17, 18, 19, 20]])
# a = np.concatenate((a1, a2), axis=0)
#              # łączy tablice jedna pod drugą, to samo co np.vstack
# print(a)
# a = np.concatenate((a1, a2), axis=1)
#              # łączy tablice jedna obok drugiej, to samo co np.hstack
# print(a)
# a = np.stack((a1, a2))  # łączy tablice w nową tablicę
# print(a)
# a = np.array(
#     [
#         [1, 2, 3, 4, 5],
#         [6, 7, 8, 9, 10],
#         [11, 12, 13, 14, 15],
#         [16, 17, 18, 19, 20],
#     ]
# )
# print(np.split(a, 2, axis=0))  # dzieli tablicę na dwie części
# print(np.split(a, 5, axis=1))  # dzieli tablicę na pięć części
# a = np.array(
#     [
#         [1, 2, 3, 4, 5, 6],
#         [6, 7, 8, 9, 10, 11],
#         [11, 12, 13, 14, 15, 16],
#         [16, 17, 18, 19, 20, 21],
#     ]
# )
# print(np.split(a, 2, axis=1))  # dzieli tablicę na dwie części


# Agregate Functions

# a = np.array(
#     [
#         [1, 2, 3, 4, 5, 6],
#         [7, 8, 9, 10, 11, 12],
#         [13, 14, 15, 16, 17, 18],
#         [19, 20, 21, 22, 23, 24],
#     ]
# )
# print(a.min())
# print(a.max())
# print(a.sum())
# print(a.mean())
# print(a.std())
# print(np.median(a))


# Numpy Random

# number = np.random.randint(100) # losowa liczba całkowita z zakresu 0-100
# print(number)
# numbers = np.random.randint(100, size=(2, 3, 4))
# # Generuje tablicę 3D z losowymi liczbami całkowitymi z zakresu 0-100
# numbers = np.random.randint(70, 100, size=(2, 3, 4))
# # Generuje tablicę 3D z losowymi liczbami całkowitymi z zakresu 70-100
# numbers = np.random.binomial(10, p=0.5, size=(5, 10))
# Generuje tablicę 2D z losowymi liczbami całkowitymi z rozkładu binomialnego
# numbers = np.random.normal(loc=170, scale=15, size=(5, 10))
# Generuje tablicę 2D z losowymi liczbami z rozkładu normalnego
# numbers = np.random.choice([1, 2, 3, 4, 5], size=(5, 10))
# Generuje tablicę 2D z losowymi liczbami z podanej listy
# print(numbers)
