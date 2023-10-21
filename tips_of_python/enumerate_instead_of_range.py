data = [1,3,-4,-7,2,-9]

for i in range(len(data)):
    if data[i] < 0:
        data[i] = 0
    
print(data)

data = [1,3,-4,-7,2,-9]

for idx, num in enumerate(data):
    if num < 0:
        data[idx] = 0

print(data)

data = [1,3,-4,-7,2,-9]

for idx, num in enumerate(data):
    if num >= 0:
        data[idx] = 1

print(data)

for idx, num in enumerate(data):
    if idx % 2 == 0:
        data[idx] = 0

print(data)