a = [5,4,1,3,2]

def bubbleSort(a: list) -> list:
    l = len(a)
    while l > 1:
        for i in range(0,l-1):
            if a[i] > a[i+1]:
                a[i], a[i+1] = a[i+1], a[i]
                print(a)
        l -= 1
    return a

print(bubbleSort(a))