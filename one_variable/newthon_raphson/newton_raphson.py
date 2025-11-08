def f(x):
    return x**2 +54/x

def f2(x):
    return x**4 -3*x**3+2

def first_derivative(f1,f3,delta):
    return (f1-f3)/(2*delta)


def second_derivative(f1,f2,f3,delta):
    return (f1+f3-2*f2)/delta**2

def newthon_raphson(x0,epsilon, delta, f):
    print(f"Initial point x0 = {x0}")
    print(f"With tolerance: {epsilon}")
    print(f"With Delta for the numeric derivatives: {delta}")
    k = 0
    f1 = f(x0+delta)
    f3 = f(x0-delta)
    derivative_f = first_derivative(f1 = f1, f3 = f3, delta=delta)
    print(f"fp {derivative_f}")
    
    while(abs(derivative_f)>epsilon):
        f2 = f(x0)
        second_derivative_f = second_derivative(f1=f1,f2=f2,f3=f3,delta=delta)
        print(f"fpp {second_derivative_f}")

        #Find the new value 
        x_new = x0 -derivative_f/second_derivative_f
        print(f"Iteration {k} give us x* = {x_new}")
        k += 1 
        #Evaluate the new derivative
        f1 = f(x_new+delta)
        f3 = f(x_new-delta)
        derivative_f = first_derivative(f1 = f1, f3 = f3, delta=delta)
        print(f"fp {derivative_f}")

        x0 = x_new
        #while()
        if k>100:
            break
    print(f"Returning the value: x = {x0}")
    return x0

if __name__ == "__main__":
    newthon_raphson(x0=1, epsilon=0.001, delta=1e-3,f=f2)