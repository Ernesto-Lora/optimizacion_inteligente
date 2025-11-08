# Division de intervalos por la mitad

def f(x):
    return x**2 +54/x

def DIPM(a,b,epsilon,f):
    k=0
    print(f'El intervalo inicial es ({a},{b})')
    xm = (a+b)/2
    l = b-a
    while(l>=epsilon):
        x1 = a+l/4;x2=b-l/4
        k += 1 
        if (f(x1) < f(xm)):
            b = xm
            xm = x1
            print(f'Iteración k = {k}')
            print(f'El intervalo es ({a},{b})')
            print(f'L = {b-a}')
        elif (f(x2) < f(xm)):
            a=xm
            xm=x2
            print(f'Iteración k = {k}')
            print(f'El intervalo es ({a},{b})')
            print(f'L = {b-a}')
        else:
            a=x1
            b=x2
            print(f'Iteración k = {k}')
            print(f'El intervalo es ({a},{b})')
            print(f'L = {b-a}')
        l = b-a
    print(f"Regresamos los valores ({a},{b})")
    return a,b

if __name__ == "__main__":

    a = float(input('Ingrese el valor de "a": '))
    b = float(input('Ingrese el valor de "b": '))
    epsilon = float(input('Ingrese el valor de "epsilon": '))
    
    DIPM(a=a, b=b, epsilon=epsilon, f=f)