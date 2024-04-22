#operatory logiczne

print(True and True) #True
print(True and False) #False
print(False and False) #False
print(False and True) #False

print(10>=5 and 3<9) #True
print(12>20 and 5<10) #False
print(3==5 and 6<1) #False

taskCompleted = True
limesOfCodeWritten = 100

if taskCompleted == True and limesOfCodeWritten >=50:
    print("Go Home")

hourOfDay = 15
if taskCompleted == True and limesOfCodeWritten >=60 and hourOfDay >=15:
    print("Go Home")


print(True or False)
print(True or True)
print(False or False) #False
print(False or True)

print( 10>=10 or 5>3)
print(5<=7 or 5==1)
print(2!=2 or 5==5)
print(1==3 or 4>10) #False
if 10>5 or "Ania" != "Ola":
    print("tru or true")

if 3==5 or "Ola"=="Ania":
    print("false or false")

#not
print(not True)#false
print(not False)#true

print(not(3==3))#false
print(not(5>10))#true
print(not(10>=6 and "Ola"!="Ania"))#false

taskCompleted = False
if taskCompleted==True:
    print("Go Home")

if not taskCompleted:
    print("Stay a bit longer and finish")

