from functools import reduce

numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

def square(n):
    return n ** 2

def even(n):
    return n % 2 == 0

def multiply(x, y):
    return x * y

squares = list(map(square, numbers))
squares1 = list(map(lambda x: x**2, numbers))

evens = list(filter(even, numbers))
evens1 = list(filter(lambda x: x % 2 == 0, numbers))

product = reduce(multiply, numbers)
product1 = reduce(lambda x,y: x * y, numbers)


print(squares)
print(squares1)
print(evens)
print(evens1)
print(product)
print(product1)
