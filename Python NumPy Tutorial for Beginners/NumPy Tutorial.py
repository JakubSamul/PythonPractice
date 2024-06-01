import numpy as np

# The Basics

# a = np.array([1, 2, 3])

# b = np.array([[9.0, 8.0, 7.0], [6.0, 5.0, 4.0]])
# print(b)

# # Get Dimension
# print(a.ndim)

# # Get Shape
# print(b.shape)

# # Get type
# print(b.dtype)

# # Get Size
# print(a.itemsize)

# # Get total size
# print(a.nbytes)


# Accessing/Changing specific elements, rows, columns, etc

# a = np.array([[1, 2, 3, 4, 5, 6, 7], [8, 9, 10, 11, 12, 13, 14]])

# # Get a specific element [r, c]
# a[1, 5]

# # Get a specific row
# a[0, :]

# # Get a specific column
# a[:, 2]

# # Getting a little more fancy [startindex:endindex:stepsize]
# a[0, 1:-1:2]

# a[1, 5] = 20

# a[:, 2] = [1, 2]
# print(a)

# b = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

# # Get specific element (work outside in)
# b[0, 1, 1]

# # replace
# b[:, 1, :] = [[9, 9], [8, 8]]


# # Initializing Different Types of Arrays

# # All 0s matrix
# np.zeros((2, 3))

# # All 1s matrix
# np.ones((4, 2, 2), dtype="int32")

# # Any other number
# np.full((2, 2), 99)

# # Any other number (full_like)
# np.full_like(a, 4)

# # Random decimal numbers
# np.random.rand(4, 2)

# # Random Integer values
# np.random.randint(-4, 8, size=(3, 3))

# # The identity matrix
# np.identity(5)

# # Repeat an array
# arr = np.array([[1, 2, 3]])
# r1 = np.repeat(arr, 3, axis=0)
# print(r1)

# # [[1. 1. 1. 1. 1.]
# #  [1. 0. 0. 0. 1.]
# #  [1. 0. 9. 0. 1.]
# #  [1. 0. 0. 0. 1.]
# #  [1. 1. 1. 1. 1.]]
# output = np.ones((5, 5))
# print(output)

# z = np.zeros((3, 3))
# z[1, 1] = 9
# print(z)

# output[1:-1, 1:-1] = z
# print(output)

# # Be careful when copying arrays!!!
# a = np.array([1, 2, 3])
# b = a.copy()
# b[0] = 100

# print(a)


# Mathematics

a = np.array([1, 2, 3, 4])


a + 2

a - 2

a * 2

a / 2

b = np.array([1, 0, 1, 0])
a + b

a**2

# Take the sin
np.sin(a)

# For a lot more (https://docs.scipy.org/doc/numpy/reference/routines.math.html)

# Linear Algebra
a = np.ones((2, 3))
print(a)

b = np.full((3, 2), 2)
print(b)

np.matmul(a, b)

# Find the determinant
c = np.identity(3)
np.linalg.det(c)

## Reference docs (https://docs.scipy.org/doc/numpy/reference/routines.linalg.html)

# Determinant
# Trace
# Singular Vector Decomposition
# Eigenvalues
# Matrix Norm
# Inverse
# Etc...
# Statistics
stats = np.array([[1, 2, 3], [4, 5, 6]])

np.min(stats)

np.max(stats, axis=1)

np.sum(stats, axis=0)
