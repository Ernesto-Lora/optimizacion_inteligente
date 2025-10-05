# bisection method
def f(x):
    return (x**2 +54/x)

def first_derivative(f1,f2,delta):
    return (f1-f2)/(2*delta)


def bisection_method(a,b, epsilon, delta, f):
    print(f"Initial interval: {[a,b]}")
    print(f"With tolerance: {epsilon}")
    print(f"With Delta for the numeric derivatives: {delta}")
    
    derivative_a = first_derivative(f1 = f(a+delta), f2 = f(a-delta), delta=delta)
    derivative_b = first_derivative(f1 = f(b+delta), f2 = f(b-delta), delta=delta)

    # if not(derivative_a<0 and derivative_b>0):
    #     print("Choose another inverval")
    #     return
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
    print(f"Returning the interval {a,b}")

    return a,b

if __name__ == "__main__":
    
    a = float(input('Enter the left bound "a": '))
    b = float(input('Enter the right bound "b": '))
    epsilon = float(input('Enter tolerance "epsilon": '))
    delta = float(input('Enter delta : '))
    bisection_method(a=a,b=b,epsilon=epsilon,delta=delta,f=f)