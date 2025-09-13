def f(x):
    return x**2 +54/x

def condicion(f1,f2,f3):
    result = f1 >= f2 and f2<=f3
    print(f' vemos que {f1:.3f} >= {f2:.3f} <= {f3:.3f} es {result}')
    return result

def busqueda_exhaustiva(a,b,n,f):
    delX = (b-a)/n
    x1 = a
    x2 = x1 + delX
    x3 = x2 + delX
    while(x3<=b):
        print(f'Estamos en {x1:.3f}, {x2:.3f}, {x3:.3f}')
        if condicion(f(x1),f(x2),f(x3)):
            print('Ya encontramos el intervalo y es:')
            print(f"{x1:.3f}, {x3:.3f}")
            return [x1,x3]
        else:
            print('Hacemos otra iteracion')
            x1 = x2
            x2 = x3
            x3 += delX
    return ('No existe el minimo entre a,b o esta en los extremos')

if __name__ == "__main__":
    #lista = busqueda_exhaustiva(-10,5,10,f)
    a = float(input('Ingrese "a": '))
    b = float(input('Ingrese "b": '))
    n = float(input('Ingrese "n": '))
    lista = busqueda_exhaustiva(a,b,n,f)      
