def fibonacci(n):
    if n==0:
        return 1
    elif n==1:
        return 1
    else:
        fibo1 = 1
        fibo2 = 1
        for i in range(n-1):
            fibo = fibo1 + fibo2
            fibo1 = fibo2
            fibo2 = fibo

        return fibo



for i in range(10):
    print(f'Fibonacci({i}): {fibonacci(i)}')

