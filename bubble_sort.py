a = [5,4,1,3,2]

def bubbleSort(a):
    l = len(a)
    while l > 1:
        finish = False
        for i in range(0,l-1):
            if a[i] > a[i+1]:
                a[i], a[i+1] = a[i+1], a[i]
                print(a)
                finish = True
        l -= 1
        if finish == False:
            break
    return a

print(bubbleSort(a))