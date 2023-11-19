def fib_seq(n: int) -> list:
    a = [1,1]
    c = 0
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return a
    else:
        while c < n-2:
            a.append(a[-1]+a[-2])
            c += 1
        return a

print(fib_seq(10))

