def f(x):
    return x**2 +54/x

def condicion1(f1,f2,f3):
    return f1>=f2 and f2>=f3

def condicion2(f1,f2,f3):
    return f1<=f2 and f2<=f3


def fase_de_acotamiento(delta,x0,f):
    k=0
    x1 = x0 - abs(delta); x2 = x0; x3 = x0 + abs(delta)
    f1 = f(x1); f2 = f(x2); f3 = f(x3) 

    if condicion1(f1=f1, f2=f2, f3=f3):
        delta = abs(delta)
        print(f'Vemos que f({x1:.3f}) = {f1:.3f} >= f({x2}) = {f2:.3f} >= f({x3:.3f})= {f3:.3f}')
        print("Se cumple, por lo tanto delta > 0")
    elif condicion2(f1=f1, f2=f2, f3=f3):
        delta = -abs(delta)
        print(f'Vemos que f({x1:.3f}) = {f1:.3f} <= f({x2}) = {f2:.3f} <= f({x3:.3f})= {f3:.3f}')
        print("Se cumple, por lo tanto delta < 0")
    else:
        print("Elige otro x0")
        return

    x_new = x0 + 2**k*delta
    print(f'Para k=0, vemos que f({x_new:.3f}) = {f(x_new):.3f} < f ({x0:.3f}) = {f(x0):.3f} es {f(x_new) < f(x0)}')
    while (f(x_new) < f(x0)):
        k+=1
        x_km1 = x_new
        x_new = x_new + 2**k*delta
        print(f'Para k = {k}, vemos que f({x_new:.3f}) = {f(x_new):.3f} < f({x_km1:.3f}) = {f(x_km1):.3f} es {f(x_new) < f(x0)}')
    print("Regresamos los valores")
    print(x_km1-(2**(k-1)+2**(k-2))*delta, x_km1)
    return x_km1-(2**(k-1)+2**(k-2))*delta, x_km1


if __name__ == "__main__":
    #print(fase_de_acotamiento(delta=0.5, x0=-5, f=f))
    delta = float(input('Ingrese "delta": '))
    x0 = float(input('Ingrese "x0": '))
    lista = fase_de_acotamiento(delta=delta, x0=x0, f=f)  
