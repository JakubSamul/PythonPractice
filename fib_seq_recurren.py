
def fib_seq_recurrent(n: int) -> int:
    if n == 0:
        a = 0
    elif n == 1:
        a = 1
    else:
        a = fib_seq_recurrent(n-1) + fib_seq_recurrent(n-2)
    return a
            
def rec(n: int) -> list:
    result = []
    for i in range(1,n+1):
        result.append(fib_seq_recurrent(i))
    return result
                 
print(rec(10))