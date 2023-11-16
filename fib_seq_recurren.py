def fib_seq_recurrent(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_seq_recurrent(n-1) + fib_seq_recurrent(n-2)
            

                 
print(fib_seq_recurrent(6))