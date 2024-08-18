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
# wszystkie funkcje matematyczne są dostępne w numpy https://numpy.org/doc/stable/reference/routines.math.html


# Array Methods

# a = np.array([1, 2, 3, 4, 5])
# a = np.append(a, [6, 7, 8])  # dodaje elementy na końcu
# a = np.insert(a, 1, [2, 2, 2, 2])  # dodaje elementy na danej pozycji
# print(a)
# a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# print(np.delete(a, 0, 0))  # usuwa elementy z danej pozycji
# print(np.delete(a, 1, 1))
