def f(x):
    return x**2 +54/x

def condicion1(f1,f2,f3):
    return f1>=f2 and f2>=f3

def condicion2(f1,f2,f3):
    return f1<=f2 and f2<=f3


def fase_de_acotamiento(delta,x0,f):
    k=0
    if condicion1(f(x0 - abs(delta)), f(x0), f(x0 + abs(delta))):
        delta = abs(delta)
        print(f'Vemos que {f(x0 - abs(delta)):.3f} >= {f(x0):.3f} >= {f(x0 + abs(delta)):.3f}')
    elif condicion1(f(x0 - abs(delta)), f(x0), f(x0 + abs(delta))):
        delta = -abs(delta)
    else:
        print("Choose another x0")
        return

    x_new = x0 + 2**k*delta
    print(f'f ({x0:.3f}) = {f(x0):.3f}, f ({x_new:.3f}) = {f(x_new):.3f}')
    while (f(x_new) < f(x0)):
        k+=1
        x_km1 = x_new
        x_new = x_new + 2**k*delta
        print(f'f({x_km1:.3f}) = {f(x_km1):.3f}, f({x_new:.3f}) = {f(x_new):.3f}')
    return x_km1-(2**(k-1)+2**(k-2))*delta, x_km1


if __name__ == "__main__":
    print(fase_de_acotamiento(0.5,-10,f))
    # comentar el impacto del valor del delta 
