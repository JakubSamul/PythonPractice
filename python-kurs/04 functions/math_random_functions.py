
import math
import random

print(type(str(12)))
print(type(str([12, 34])))

number = int("123")
print(type(number))

number += 10 
print(number)
print("123" + "10")

floatNum = float("45.67")
print(type(floatNum))
floatNum =  floatNum * 2
print(floatNum)

print(abs(9))
print(abs(-9.1))

print(math.ceil(11.001)) #12
print(math.ceil(-13.001)) #-13
print(math.ceil(9.999999)) #10

print(math.floor(11.001)) #11
print(math.floor(11.999)) #11
print(math.floor(5.12)) #5
print(math.floor(-5.99999)) #-6

print(max(10, 1, -1, 55, 91, 65)) #91
print(max([10, 1, -1, 55, 91, 65])) #91
print(max((10, 1, -1, 55, 91, 65))) #91

print(min((10, 1, -1, 55, 91, 65))) #-1
print(min([10, 1, -1, 55, 91, 65])) #-1
print(min((10, 1, -1, 55, 91, 65))) #-1

print(4 ** 3) #64
print(pow(4, 3)) #64

print(math.sqrt(128)) #11.31.....

print( round(12.7891234, 3) ) # 12.789
print( round(12.7891234, 2) ) # 12.79
print( round(12.7891234, 1) ) # 12.8

print(random.random())
print(random.random()*100)
print(int(random.random()*100))

print(random.choice([0,1,2,3,4]))
print(random.choice(("Ola","Ania","Ada")))

print(random.randrange(-10, 30, 5))

listData = [0,1,2,3,4,5,6]
random.shuffle(listData)

print(listData)





