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

a_nul = np.array([[[1, 2, 3, 1], [4, 5, 6, 1], [7, 8, 9, 1]], [[1, 2, 3, 1], [4, 5, 6, 1], [7, 8, 9, 1]]])
print(a_nul[0])
print(a_nul[0, 1])
print(a_nul.shape)
print(a_nul.ndim)
print(a_nul.size)
print(a_nul.dtype)
