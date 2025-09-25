# Fibonacci Search Method

def fibonacci_number(n):
    if n<=1:
        return 1
    else:
        fibo1 = 1
        fibo2 = 1
        for i in range(n-1):
            fibo = fibo1 + fibo2
            fibo1 = fibo2
            fibo2 = fibo

        return fibo


def f(x):
    return x**2 +54/x

def custom_print(a, b, k, i):
    print(f"Iteration {i}. k = {k}.")
    print(f"Interval found: [{a:.6f}, {b:.6f}]")
    print(f"Interval length (L): {b - a:.6f}")
    print("-" * 40)


def fibonacci_search(a,b,n,f):
    print(f"The initial interval is [{a:.6f}, {b:.6f}]")
    k = 2
    l = b-a
    lk = fibonacci_number(n-k+1)/fibonacci_number(n+1)*l
    x1 = a+lk
    x2 = b-lk
    fx1 = f(x1)
    fx2 = f(x2)
    i=1
    while(k != n+1):
        k += 1
        lk = fibonacci_number(n-k+1)/fibonacci_number(n+1)*l

        if (fx1 > fx2):
            a = x1

            x1 = x2
            fx1 = fx2
            x2 = b-lk
            fx2 = f(x2)
            custom_print(a,b,k-1, i)
            
        else:
            b = x2
            
            x2 = x1
            fx2 = fx1
            x1 = a+lk
            fx1 = f(x1)
            custom_print(a,b,k-1,i)
        i += 1 


    print(f"Returning the values [{a:.6f}, {b:.6f}]")
    return a,b

if __name__ == "__main__":

    a = float(input('Enter the value of "a" (lower bound): '))
    b = float(input('Enter the value of "b" (upper bound): '))
    n = int(input('Enter the number of iterations "n": '))

    fibonacci_search(a=a, b=b, n=n, f=f)


