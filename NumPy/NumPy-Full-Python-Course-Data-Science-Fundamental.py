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

x_values = np.linspace(0, 1000, 1001)
print(x_values)
