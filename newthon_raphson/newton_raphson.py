def f(x):
    return x**2 +54/x

def first_derivative(f1,f3,delta):
    return (f1-f3)/(2*delta)

def analitic_first_derivative():
    return 2

def second_derivative(f1,f2,f3,delta):
    return (f1+f3-2*f2)/delta**2

def newthon_raphson(x0,epsilon, delta, f):
    f1 = f(x0+delta)
    f3 = f(x0-delta)
    derivative_f = first_derivative(f1 = f1, f3 = f3, delta=delta)
    
    while(abs(derivative_f)>epsilon):
        f2 = f(x0)
        second_derivative_f = second_derivative(f1=f1,f2=f2,f3=f3,delta=delta)
        #print(derivative_f)
        #print(second_derivative_f)


        #Find the new value 
        x_new = x0 -derivative_f/second_derivative_f

        #Evaluate the new derivative
        f1 = f(x_new+delta)
        f3 = f(x_new-delta)
        derivative_f = first_derivative(f1 = f1, f3 = f3, delta=delta)

        print(f'The current x is: {x_new}')
        x0 = x_new
        #while()

    return 

if __name__ == "__main__":
    newthon_raphson(x0=1, epsilon=1e-3, delta=1e-5,f=f)