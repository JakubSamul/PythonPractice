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

a = np.array([[1, 2, 3, 4, 5, 6, 7], [8, 9, 10, 11, 12, 13, 14]])

# Get a specific element [r, c]
a[1, 5]

# Get a specific row
a[0, :]

# Get a specific column
a[:, 2]

# Getting a little more fancy [startindex:endindex:stepsize]
a[0, 1:-1:2]

a[1, 5] = 20

a[:, 2] = [1, 2]
print(a)

b = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

# Get specific element (work outside in)
b[0, 1, 1]

# replace
b[:, 1, :] = [[9, 9], [8, 8]]
