# bisection method
def f(x):
    return (x**2 +54/x)

def fxy(x1,x2):
    return (x1**2 + x2 - 11)**2 + (x1 + x2**2 - 7)**2


def first_derivative(f1,f2,delta): # numeric_derivative
    return (f1-f2)/(2*delta)

def bisection_method(a,b, epsilon, delta, f):
    print(f"Initial interval: {[a,b]}")
    print(f"With tolerance: {epsilon}")
    print(f"With Delta for the numeric derivatives: {delta}")
    
    derivative_a = first_derivative(f1 = f(a+delta), f2 = f(a-delta), delta=delta)
    derivative_b = first_derivative(f1 = f(b+delta), f2 = f(b-delta), delta=delta)

    if not(derivative_a<0 and derivative_b>0):
        print("Choose another inverval")
        return
    k = 1
    while(True): # Do-While implementation
        z = (a+b)/2
        f1 = f(z+delta)
        f2 = f(z-delta)
        derivative_f = first_derivative(f1 = f1, f2 = f2, delta=delta)

        if derivative_f< 0:
            a = z
        else:
            b=z

        print(f"In the iteration {k} the current interval is [{a},{b}]")
        if k>100:
            break
        if abs(derivative_f)<epsilon:
            break
        k +=1 
    print(f"Returning x = {a}, f = {f(a)}")

    return a,f(a)

if __name__ == "__main__":
    
    def g1(alpha): return fxy(alpha,4)
    def g2(alpha): return fxy(2.083,4+alpha)
    def g3(alpha): return fxy(2.083+alpha, 2.408)
    def g4(alpha): return fxy(2.881+0.448*alpha, 2.408-0.894*alpha)
    
    bisection_method(a=-100,b=100,epsilon=0.001,delta=0.001,f=g4)
